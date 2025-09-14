from pydantic import BaseModel

class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

class TagCreate(BaseSchema):
    tag: str
    
class TagRead(BaseSchema):
    id:int
    tag: str
    