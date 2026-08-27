from pydantic import BaseModel
from typing import Dict, Any


class MatchRequest(BaseModel):
    resume: Dict[str, Any]
    job_description: str