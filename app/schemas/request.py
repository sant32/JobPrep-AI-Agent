from pydantic import BaseModel
from typing import List, Optional

class JobPrepRequest(BaseModel):
    job_description: str
    user_skills: List[str]
    resume_text: Optional[str] = ""
    prep_days: Optional[int] = 7