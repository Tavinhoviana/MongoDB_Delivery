import pytest
from .registry_order_validator import registry_order_validator

def test_registr_order_validator():
    body = {
        "data": {
            "name": "Otavio",
            "address": "muhlenstr",
            "cupom": False,
            "items": [
                { "item": "refrigerante", "quantidade": 2},
                { "item": "pizza", "quantidade": 1}
            ]
        }
    }

    registry_order_validator(body)

def test_registr_order_validator_with_error():
    body_with_error = {
        "data": {
            "name": "Otavio",
            "address": "muhlenstr",
            "cupom": "error",
            "items": [
                { "item": "refrigerante", "quantidade": 2},
                { "item": "pizza", "quantidade": 1}
            ]
        }
    }
    with pytest.raises(Exception):
        registry_order_validator(body_with_error)
