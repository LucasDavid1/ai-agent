def get_tools():
    tools = [
        {
            "type": "function",
            "function": {
                "name": "add",
                "description": "Adds two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "description": "First number"
                        },
                        "b": {
                            "type": "number",
                            "description": "Second number"
                        },
                    },
                    "required": ["a", "b"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "subtract",
                "description": "Subtracts second number from the first",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "description": "First number"
                        },
                        "b": {
                            "type": "number",
                            "description": "Number to subtract from the first"
                        },
                    },
                    "required": ["a", "b"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "multiply",
                "description": "Multiplies two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "description": "First number"
                        },
                        "b": {
                            "type": "number",
                            "description": "Second number"
                        },
                    },
                    "required": ["a", "b"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "divide",
                "description": "Divides first number by second",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "description": "First number"
                        },
                        "b": {
                            "type": "number",
                            "description": "Number to divide the first number by"
                        },
                    },
                    "required": ["a", "b"]
                },
            },
        },
    ]

    return tools
