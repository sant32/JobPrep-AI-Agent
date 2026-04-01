from pydantic import BaseModel
from typing import List
from app.schemas.outputs import (JDAnalysis, CandidateProfile, SkillGap, Roadmap, ProjectSuggestion, LearningResource)



class FinalJobResponse(BaseModel):
    jd_analysis: JDAnalysis
    candidate_profile: CandidateProfile 
    skill_gap: SkillGap
    roadmap: Roadmap
    interview_topics: List[str]
    project_suggestions: List[ProjectSuggestion]
    resume_suggestions: List[str]
    learning_resources: List[LearningResource]