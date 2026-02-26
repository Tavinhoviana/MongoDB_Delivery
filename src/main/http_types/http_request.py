from typing import Dict

class HttpRequest: 
    def __init__(
            self, 
            body: Dict = None,
            header: Dict = None,
            params: Dict = None
        ) -> None:
        self.body = body
        self.header = header
        self.params = params
