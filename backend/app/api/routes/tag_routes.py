from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.utils.api_response import response_error, response_success
from app.application.tag_service import TagService
from app.infrastructure.database import open_session
from app.schemas.tag_schema import TagRead

router = APIRouter(prefix="/tags", tags=["tags"])

@router.get("/", response_model = TagRead)
def get_all_tags(db:Session = Depends(open_session)):
    
    try:
    
        tag_service = TagService(db)
        list_tags = tag_service.get_all_tags()
            
        return response_success(
            data = [jsonable_encoder(tag) for tag in list_tags],
            status_code = status.HTTP_200_OK
        )
    
    except HTTPException as error:
        return response_error(
            message="Erro ao buscar Tags"
        )