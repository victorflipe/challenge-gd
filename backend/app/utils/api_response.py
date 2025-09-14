from fastapi.responses import JSONResponse
from fastapi import status
from typing import Any, Optional

def response_success(
    data: Any = None,
    message: str = None,
    status_code: int = status.HTTP_200_OK
) -> JSONResponse:
    """Retorna mensagem de sucesso"""
    
    content = {
        "response": {
            "data": data
        }
    }
    
    if not message is None:
        content["response"]["message"] = message
    
    print(f"Content criado: {content}")
    
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
        "response": {
            "message": message,
            "details": details
        }
    }
    
    return JSONResponse(
        status_code = status_code,
        content = content
    )