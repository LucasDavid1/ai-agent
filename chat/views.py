from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from chat.services import determine_function_and_call


@csrf_exempt
@require_http_methods(["POST"])
def chat_view(request):
    try:
        data = json.loads(request.body)
        user_input = data.get('message', '')

        result = determine_function_and_call(user_input)

        response = {
            'status': 'success',
            'result': result
        }

        return JsonResponse(response)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
