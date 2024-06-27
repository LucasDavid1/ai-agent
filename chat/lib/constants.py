import chat.calculations as chat_calculations
import chat.providers as chat_providers
from chat.utils import get_tools

GROQ_MODEL = "llama3-70b-8192"

FUNCTION_DICT_LEGACY = {
    "add": chat_calculations.add,
    "subtract": chat_calculations.subtract,
    "multiply": chat_calculations.multiply,
    "divide": chat_calculations.divide
}

FUNCTION_DICT = {
    "create_artist": chat_providers.create_artist,
    "create_band": chat_providers.create_band,
    "create_album": chat_providers.create_album,
    "search_music": chat_providers.search_music,
    "search_artists": chat_providers.search_artists,
    "search_bands": chat_providers.search_bands,
    "get_band_albums": chat_providers.get_band_albums,
    "get_albums_by_genre": chat_providers.get_albums_by_genre,
    "get_artist_bands": chat_providers.get_artist_bands
}

SYSTEM_PROMPT_OLD = f"You are an IT bot that receives instructions and returns which function must be used with the arguments. These are the available functions: {list(FUNCTION_DICT.keys())}. You only return the function name and the arguments"
SYSTEM_PROMPT_LEGACY = f"You are an IT bot that receives instructions and returns which function must be used with the arguments. These are the available functions: {get_tools()}. Return only the function name and arguments like: func_name, arg1, arg2, arg3, arg4, arg5"
SYSTEM_PROMPT = f"""
You are an AI assistant for a music database. You can perform the following functions:
{get_tools()}
When a user asks a question, respond with the appropriate function call in JSON format.
For example:
- If asked "Create a new artist named John Doe who plays guitar from USA", respond with:
  dict: "function": "create_artist", "arguments": "name": "John Doe", "instrument": "guitar", "country": "USA"
Always respond with just the function call in JSON format, nothing else.
"""