def get_tools_legacy():
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


def get_tools():
    tools = [
        {
            "type": "function",
            "function": {
                "name": "create_artist",
                "description": "Creates a new artist",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Artist's name"},
                        "instrument": {"type": "string", "description": "Artist's main instrument"},
                        "country": {"type": "string", "description": "Artist's country"}
                    },
                    "required": ["name", "instrument", "country"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "create_band",
                "description": "Creates a new band",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Band's name"},
                        "formation_year": {"type": "integer", "description": "Year the band was formed"},
                        "genre": {"type": "string", "description": "Band's primary genre"},
                        "member_ids": {"type": "array", "items": {"type": "integer"}, "description": "List of artist IDs who are members of the band"}
                    },
                    "required": ["name", "formation_year", "genre", "member_ids"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "create_album",
                "description": "Creates a new album",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Album title"},
                        "release_date": {"type": "string", "description": "Album release date (YYYY-MM-DD)"},
                        "genre": {"type": "string", "description": "Album's genre"},
                        "band_id": {"type": "integer", "description": "ID of the band"}
                    },
                    "required": ["title", "release_date", "genre", "band_id"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_music",
                "description": "Searches for music by title, band, or artist",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query"}
                    },
                    "required": ["query"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_artists",
                "description": "Searches for artists by name, instrument, or country",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "General search query (optional)"
                        },
                        "instrument": {
                            "type": "string",
                            "description": "Specific instrument to search for (optional)"
                        },
                        "country": {
                            "type": "string",
                            "description": "Specific country to search for (optional)"
                        }
                    },
                    "required": []
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_bands",
                "description": "Searches for bands by name, genre, formation year, or member name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "General search query for band name or member name (optional)"
                        },
                        "genre": {
                            "type": "string",
                            "description": "Specific genre to search for (optional)"
                        },
                        "formation_year": {
                            "type": "integer",
                            "description": "Specific year the band was formed (optional)"
                        }
                    },
                    "required": []
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_band_albums",
                "description": "Gets all albums by a band",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "band_id": {"type": "integer", "description": "ID of the band"}
                    },
                    "required": ["band_id"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_albums_by_genre",
                "description": "Gets all albums of a specific genre",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "genre": {"type": "string", "description": "Genre to search for"}
                    },
                    "required": ["genre"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_artist_bands",
                "description": "Gets all bands an artist is a member of",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artist_id": {"type": "integer", "description": "ID of the artist"}
                    },
                    "required": ["artist_id"]
                },
            },
        },
    ]
    return tools
