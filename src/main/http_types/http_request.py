from typing import Dict

class HttpRequest: 
    def __init__(
            self, 
            body: Dict = None,
            header: Dict = None,
            path_params: Dict = None,
            query: dict = None
        ) -> None:
        self.body = body
        self.header = header
        self.params = path_params
        self.query = query
