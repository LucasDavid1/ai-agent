# AI Agent Django Project

This Django project implements an AI agent that uses the Groq API to process user inputs and perform mathematical operations based on natural language requests.

## Project Overview

The AI agent interprets user queries, determines the appropriate mathematical function to use, and returns the result. It leverages the Groq API with the LLaMA 3 70B model for natural language processing.

## Key Features

- Natural language processing of mathematical queries
- Integration with Groq API
- Dynamic function calling based on AI interpretation
- RESTful API endpoint for easy integration

## Setup

1. Clone the repository
2. make up


## Usage

Send a POST request to `http://localhost:8000/chat/` with a JSON body:

```json
{
 "message": "need to know how many doctors we need if we have 500 patients and a doctor can attend 5 patients"
}
```
The server will respond with:
```json
{
    "status": "success",
    "result": 100.0
}
```

Here's a README.md in markdown format explaining the Django project with the functionality you described:
markdownCopy# AI Agent Django Project

This Django project implements an AI agent that uses the Groq API to process user inputs and perform mathematical operations based on natural language requests.

## Project Overview

The AI agent interprets user queries, determines the appropriate mathematical function to use, and returns the result. It leverages the Groq API with the LLaMA 3 70B model for natural language processing.

## Key Features

- Natural language processing of mathematical queries
- Integration with Groq API
- Dynamic function calling based on AI interpretation
- RESTful API endpoint for easy integration

## Setup

1. Clone the repository
2. Install dependencies:
pip install -r requirements.txt
Copy3. Set up environment variables:
- `GROQ_API_KEY`: Your Groq API key
- Other necessary database and Django settings

4. Run migrations:
python manage.py migrate
Copy5. Start the Django server:
python manage.py runserver
Copy
## Usage

Send a POST request to `http://localhost:8000/chat/` with a JSON body:

```json
{
 "message": "need to know how many doctors we need if we have 500 patients and a doctor can attend 5 patients"
}
```
The server will respond with:
```json
{
    "status": "success",
    "result": 100.0
}
```
##How It Works

1. The user sends a natural language query to the /chat/ endpoint.
2. The query is sent to the Groq API using the LLaMA 3 70B model.
3. The AI interprets the query and determines the appropriate mathematical function to use.
4. The determined function is called with the extracted parameters.
5. The result is returned to the user.

##Project Structure

- chat/services.py: Contains the core logic for processing queries and calling functions.
- chat/lib/constants.py: Defines the FUNCTION_DICT and SYSTEM_PROMPT.
- chat/views.py: Handles the API endpoint and request processing.
- ai_agent/settings.py: Contains project settings and API keys.

## Available Functions and Extensibility

The core idea of this project is to create a flexible system where any custom function can be defined and utilized by the AI. The AI is designed to interpret user queries and correctly employ these functions based on the context.

### Current Function Set

The project comes with a set of basic mathematical operations as examples:

- Addition
- Subtraction
- Multiplication
- Division

These functions are defined in `FUNCTION_DICT` in `constants.py`.

### Extending with Custom Functions

The true power of this system lies in its extensibility. You can define any custom function that your AI agent should be able to use. The AI will then interpret user queries and determine when and how to use these functions. For example, you could add functions for:

- Complex mathematical operations
- Data processing tasks
- External API calls
- Database queries
- Custom business logic

### Adding New Functions

To add new functions to your AI agent's capabilities:

1. Define the new function in `chat/functions.py`
2. Add the function to `FUNCTION_DICT` in `constants.py`
3. Update the `SYSTEM_PROMPT` in `constants.py` to include information about the new function. This helps the AI understand when and how to use the new function.

### AI Adaptation

The LLM (Large Language Model) used in this project is designed to adapt to the functions you define. By updating the `SYSTEM_PROMPT`, you provide the AI with the necessary context to understand and utilize your custom functions appropriately.

This flexibility allows the AI agent to handle a wide range of tasks beyond simple calculations, limited only by the functions you choose to implement and the capabilities of the LLM in interpreting user requests.

Note
Ensure that your Groq API key is kept secure and not shared publicly. Always use environment variables for sensitive information.