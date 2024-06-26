import chat.calculations as chat_calculations


FUNCTION_DICT = {
    "add": chat_calculations.add,
    "subtract": chat_calculations.subtract,
    "multiply": chat_calculations.multiply,
    "divide": chat_calculations.divide
}

SYSTEM_PROMPT = f"You are an IT bot that receives instructions and returns which function must be used with the arguments. These are the available functions: {list(FUNCTION_DICT.keys())}. You only return the function name and the arguments"