from src.main.http_types.http_response import HttpResponse
from .types.http_not_found import HttpNotFoundError
from .types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            status_code=error.status_code
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "server error",
                "detail": str(error)
            }]
        }
    )
