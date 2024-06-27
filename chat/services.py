from groq import Groq
import json

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
            return output['function'], output['arguments']
        except json.JSONDecodeError:
            return "parse_error", {}

    def determine_function_and_call(self, user_input):
        model_output = self.get_completion(user_input)
        func_name, args = self.process_output(model_output)
        print("model_output", model_output)
        print("func_name", func_name)
        print("args", args)
        if func_name == "parse_error":
            return "Error: Could not parse the model output"
        return call_function(func_name, **args)
