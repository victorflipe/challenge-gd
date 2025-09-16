from fastapi.responses import JSONResponse
from fastapi import status
from typing import Any, Optional

def response_success(
    data: Any = None,
    message: str = None,
    status_code: int = status.HTTP_200_OK,
    pagination: Optional[dict] = None
) -> JSONResponse:
    """Retorna mensagem de sucesso"""
    
    content = {
        "data": data,
        "message": message
    }

    if pagination:
        content["pagination"] = pagination
    
    return JSONResponse(
        status_code=status_code,
        content = content
    )
    
def response_error(
    message: str = "Erro ao executar ação",
    status_code : int = status.HTTP_400_BAD_REQUEST,
    details: Optional[Any] = None
) -> JSONResponse:
    """Retorna mensagem de erro"""
    
    content = {
        "message": message,
        "details": details
    }
    
    return JSONResponse(
        status_code = status_code,
        content = content
    )