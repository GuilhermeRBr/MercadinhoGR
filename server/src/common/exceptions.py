from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error = exc.errors()[0]
    field = error["loc"][-1]
    error_type = error["type"]

    if error_type == "string_too_long":
        message = f"O campo '{field}' excede o tamanho máximo permitido."
    elif error_type == "string_too_short":
        message = f"O campo '{field}' tem tamanho menor do que o permitido."
    elif error_type == "missing":
        message = f"O campo '{field}' é obrigatório."
    else:
        message = f"Erro no campo '{field}'."

    return JSONResponse(
        status_code=422,
        content={"detail": message},
    )
