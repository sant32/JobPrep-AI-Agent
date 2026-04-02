from app.llm.model import get_llm, get_google_llm
from app.graph.prompts import (
    JD_EXTRACTOR_PROMPT,
    CANDIDATE_PROFILE_PROMPT,
    SKILL_GAP_PROMPT,
    PLANNER_PROMPT,
    ROADMAP_PROMPT,
    INTERVIEW_TOPICS_PROMPT,
    PROJECT_RECOMMENDER_PROMPT,
    RESUME_ALIGNMENT_PROMPT,
    LEARNING_RESOURCES_PROMPT,
    TAVILY_SEARCH_PROMPT
)


from app.schemas.outputs import (
    JDAnalysis,
    CandidateProfile,
    SkillGap,
    PlanContext,
    Roadmap,
    InterviewTopics,
    ProjectSuggestions,
    ResumeSuggestions,
    LearningResources,
    TavilyQuery
)

llm = get_llm()
google_llm = get_google_llm()

planner_chain = PLANNER_PROMPT | llm.with_structured_output(PlanContext)

jd_extractor_chain = JD_EXTRACTOR_PROMPT | llm.with_structured_output(JDAnalysis)

candidate_profile_chain = CANDIDATE_PROFILE_PROMPT | llm.with_structured_output(CandidateProfile)

skill_gap_chain = SKILL_GAP_PROMPT | llm.with_structured_output(SkillGap)

roadmap_chain = ROADMAP_PROMPT | google_llm.with_structured_output(Roadmap)

interview_topics_chain = INTERVIEW_TOPICS_PROMPT | llm.with_structured_output(InterviewTopics)

project_recommender_chain = PROJECT_RECOMMENDER_PROMPT | llm.with_structured_output(ProjectSuggestions)

resume_alignment_chain = RESUME_ALIGNMENT_PROMPT | llm.with_structured_output(ResumeSuggestions)

learning_resources_chain = LEARNING_RESOURCES_PROMPT | llm.with_structured_output(LearningResources)

query_tavily_chain = TAVILY_SEARCH_PROMPT | llm.with_structured_output(TavilyQuery)

