from typing import Dict
from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def insert_document(self, document: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    @abstractmethod
    def insert_list_of_documents(self, list_of_documents: list) -> None:
        pass

    @abstractmethod
    def select_many(self, doc_filter: Dict) -> list:
        pass

    @abstractmethod
    def select_one(self, doc_filter: Dict) -> Dict:
        pass

    @abstractmethod
    def select_many_with_properties(self, doc_filter: Dict) -> list:
        pass

    @abstractmethod
    def select_if_property_exist(self) -> Dict:
        pass

    @abstractmethod
    def select_by_object_id(self, object_id: str) -> Dict:
        pass

    @abstractmethod
    def edit_registry(self) -> None:
        pass

    @abstractmethod
    def edit_many_registries(self) -> None:
        pass

    @abstractmethod
    def edit_registry_with_increment(self) -> None:    
        pass

    @abstractmethod
    def edit_registry_with_decrement(self) -> None:
        pass

    @abstractmethod
    def delete_registry(self) -> None:
        pass

    @abstractmethod
    def delete_many_registry(self) -> None:
        pass
