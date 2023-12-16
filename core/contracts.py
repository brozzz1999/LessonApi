USER_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}

    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

SINGLE_USER_SUPPORT = {
    "url": "string",
    "text": "string"
}

RESOURCE_DATA_SHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"}
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}

SINGLE_RESOURCE_SUPPORT_SHEMA = {
    "url": "string",
    "text": "string"
}
