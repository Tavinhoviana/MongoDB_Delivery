from typing import Dict
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from .registry_order import RegistryOrder

class OrderRepositoryMock:
    def __init__(self) -> None:
        self.insert_document_att = {}

    def insert_document(self, document: Dict):
        self.insert_document_att["document"] = document

class OrderRepositoryMockError:
    def insert_document(self, document: Dict):
        self.insert_document_att["document"] = document
        raise Exception["error aqui"]

def test_registry():
    repo = OrderRepositoryMock()
    registry_order = RegistryOrder(repo)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "Otavio",
                "address": "muhlenstr",
                "cupom": False,
                "items": [
                    { "item": "refrigerante", "  quantidade": 2},
                    { "item": "pizza", "  quantidade": 1}

                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert "name" in repo.insert_document_att["document"]
    assert "address" in repo.insert_document_att["document"]
    assert "created_at" in repo.insert_document_att["document"]

    assert response.status_code == 201
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["type"] == "Order"