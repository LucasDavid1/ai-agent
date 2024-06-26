import chat.calculations as chat_calculations
from chat.utils import get_tools

GROQ_MODEL = "llama3-70b-8192"

FUNCTION_DICT = {
    "add": chat_calculations.add,
    "subtract": chat_calculations.subtract,
    "multiply": chat_calculations.multiply,
    "divide": chat_calculations.divide
}

SYSTEM_PROMPT_OLD = f"You are an IT bot that receives instructions and returns which function must be used with the arguments. These are the available functions: {list(FUNCTION_DICT.keys())}. You only return the function name and the arguments"
SYSTEM_PROMPT = f"You are an IT bot that receives instructions and returns which function must be used with the arguments. These are the available functions: {get_tools()}. Return only the function name and arguments like: func_name, arg1, arg2, arg3, arg4, arg5"