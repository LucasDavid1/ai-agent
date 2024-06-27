from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.serializers import serialize
from django.db.models.query import QuerySet

import json

from chat.services import GroqHandler


@csrf_exempt
@require_http_methods(["POST"])
def chat_view(request):
    try:
        data = json.loads(request.body)
        user_input = data.get('message', '')

        results = GroqHandler().determine_function_and_call(user_input=user_input)

        def serialize_result(result):
            if isinstance(result, QuerySet):
                return json.loads(serialize('json', result))
            elif hasattr(result, '_meta'):
                return json.loads(serialize('json', [result]))[0]
            elif isinstance(result, list):
                return [serialize_result(item) for item in result]
            elif isinstance(result, dict):
                return {k: serialize_result(v) for k, v in result.items()}
            else:
                return result

        serialized_results = serialize_result(results)

        response = {
            'status': 'success',
            'result': serialized_results
        }

        return JsonResponse(response, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
