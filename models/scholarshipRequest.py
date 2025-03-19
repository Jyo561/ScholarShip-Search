from pydantic import BaseModel
from typing import Optional

class ScholarshipRequest(BaseModel):
    caste: str
    religion: str
    converted: Optional[bool] = None
