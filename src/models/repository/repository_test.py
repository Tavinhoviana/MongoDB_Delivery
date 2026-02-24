import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.collect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interaction with db")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "ola": "mundo" }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interaction with db")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{ "estou": "aqui" }, { "estou": "la", }, { "estou": "em todo lugar" }]
    orders_repository.insert_list_of_documents(my_doc)
