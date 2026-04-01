from typing import TypedDict, List, Dict, Any, Optional
from app.schemas.outputs import (
    JDAnalysis,
    CandidateProfile,
    SkillGap,
    PlanContext,
    Roadmap,
    ProjectSuggestion,
    LearningResource
)


class AgentState(TypedDict):
    job_description: str
    user_skills: List[str]
    resume_text: Optional[str]
    prep_days: int


    jd_analysis: JDAnalysis
    candidate_profile: CandidateProfile
    skill_gap: SkillGap
    plan_context: PlanContext


    roadmap: Roadmap
    interview_topics: List[str]
    project_suggestions: List[ProjectSuggestion]
    resume_suggestions: List[str]
    learning_resources: List[LearningResource]

    final_response: Dict[str, Any]

