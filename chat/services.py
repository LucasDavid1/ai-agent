from groq import Groq
import json
from datetime import datetime

from chat.lib.constants import FUNCTION_DICT, SYSTEM_PROMPT, GROQ_MODEL
import ai_agent.settings as settings


def call_function(func_name, *args, **kwargs):
    converted_args = []
    for arg in args:
        if isinstance(arg, str) and arg.isnumeric():
            converted_args.append(float(arg))
        else:
            converted_args.append(arg)
    
    if func_name in FUNCTION_DICT:
        return FUNCTION_DICT[func_name](*converted_args, **kwargs)
    else:
        return "Function not found"
    

class GroqHandler:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = GROQ_MODEL

    def get_completion(self, user_input):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=self.model,
        )
        return chat_completion.choices[0].message.content

    def process_output_legacy(self, model_output):
        table = str.maketrans('', '', ',')
        parts = model_output.split()
        parts = [item.translate(table) for item in parts]
        func_name = parts[0]
        args = list(map(int, parts[1:]))
        return func_name, args
    
    def process_output(self, model_output):
        try:
            output = json.loads(model_output)
            if isinstance(output, list):
                return output
            elif isinstance(output, dict) and 'function' in output:
                return [output]
            else:
                return "parse_error", {}
        except json.JSONDecodeError:
            return "parse_error", {}


    def execute_operations(self, processed_output):
        results = []
        context = {
            'created_artists': [],
            'created_band': None
        }

        for operation in processed_output:
            func_name = operation['function']
            args = operation['arguments']
            
            if func_name == 'create_artist':
                result = call_function(func_name, **args)
                context['created_artists'].append(result)
            elif func_name == 'create_band':
                member_ids = args.get('member_ids', [])
                args['member_ids'] = [
                    context['created_artists'][i-1].id 
                    for i in member_ids 
                    if 0 < i <= len(context['created_artists'])
                ]
                result = call_function(func_name, **args)
                context['created_band'] = result
            elif func_name == 'create_album':
                if 'release_date' in args:
                    args['release_date'] = datetime.strptime(args['release_date'], "%Y-%m-%d").date()
                if 'band_id' in args and isinstance(args['band_id'], int):
                    args['band_id'] = context['created_band'].id if context['created_band'] else args['band_id']
                result = call_function(func_name, **args)
            else:
                result = call_function(func_name, **args)
            
            results.append(result)

        return results

    def determine_function_and_call(self, user_input):
        model_output = self.get_completion(user_input)
        print("model_output", model_output)
        
        processed_output = self.process_output(model_output)
        if processed_output == "parse_error":
            return "Error: Could not parse the model output"
        
        return self.execute_operations(processed_output)
