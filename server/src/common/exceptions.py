from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error = exc.errors()[0]
    loc = error["loc"]

    # ignora termos genéricos
    ignored = {"body", "query", "path"}

    field = next(
        (
            item
            for item in reversed(loc)
            if isinstance(item, str) and item not in ignored
        ),
        None,
    )

    error_type = error["type"]

    if field:
        if error_type == "string_too_long":
            message = f"O campo '{field}' excede o tamanho máximo permitido."
        elif error_type == "string_too_short":
            message = f"O campo '{field}' tem tamanho menor do que o permitido."
        elif error_type == "missing":
            message = f"O campo '{field}' é obrigatório."
        elif error_type == "int_parsing":
            message = f"O campo '{field}' deve ser um número inteiro válido."
        elif error_type == "float_parsing":
            message = f"O campo '{field}' deve ser um número válido."
        elif error_type == "greater_than":
            message = f"O campo '{field}' deve ser maior que zero."
        elif error_type == "greater_than_equal":
            message = (
                f"O campo '{field}' deve ser maior ou igual ao valor mínimo permitido."
            )
        else:
            message = f"Erro no campo '{field}'."
    else:
        message = "Erro nos dados enviados."

    return JSONResponse(
        status_code=422,
        content={"detail": message},
    )
