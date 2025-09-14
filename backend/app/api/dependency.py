from fastapi import Depends
from sqlalchemy.orm import Session
from dataclasses import dataclass

from app.infrastructure.database import open_session
from app.schemas.user_schema import UserRead
from app.api.auth import get_current_user

@dataclass
class CommonDeps:
    db: Session
    current_user: UserRead
    
def get_common_deps(
    db:Session = Depends(open_session),
    current_user: UserRead = Depends(get_current_user)
)-> CommonDeps:
    return CommonDeps(db=db, current_user=current_user)