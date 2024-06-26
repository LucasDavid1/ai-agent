from groq import Groq

from chat.lib.constants import FUNCTION_DICT, SYSTEM_PROMPT
import ai_agent.settings as settings


def call_function(func_name, *args, **kwargs):
    # Convert arguments to numbers if possible
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


def determine_function_and_call(user_input):
    client = Groq(
        api_key=settings.GROQ_API_KEY,
    )

    chat_completion = client.chat.completions.create(
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
        model="llama3-70b-8192",
    )
    model_output = chat_completion.choices[0].message.content

    parts = model_output.split()
    func_name = parts[0]
    args = list(map(int, parts[1:]))

    result = call_function(func_name, *args)
    return result
