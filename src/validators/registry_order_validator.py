from cerberus import Validator

def registry_order_validator(body: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": { "type": "string", "required": True },
                "address": { "trpe": "string", "required": True},
                "cupom": { "type": "boolean", "required": True},
                "items": {
                    "type": "list"},
                    "schema": {
                        "type": "dict",
                        "schema": {
                            "items": { "type": "string", "required": True},
                            "quantidade": { "type": "integer", "required": True}
                        }
                    }
            }
        }
    })

    response = body_validator.validate(body)
    if response is False:
        raise Exception(body_validator.errors)
