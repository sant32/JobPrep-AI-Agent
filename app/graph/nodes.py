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
    LEARNING_RESOURCES_PROMPT
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
    LearningResources
)

llm = get_llm()
google_llm = get_google_llm()


def input_parser(state):
    return {
        "job_description": state["job_description"],
        "user_skills": state.get("user_skills", []),
        "resume_text": state.get("resume_text", ""),
        "prep_days": state.get("prep_days", 7)
    }

def JD_extractor(state):
    structured_llm = llm.with_structured_output(JDAnalysis)

    prompt = JD_EXTRACTOR_PROMPT.format(
        job_description=state["job_description"]
    )

    result = structured_llm.invoke(prompt)

    return {
        "jd_analysis": result
    }


def candidate_profile_extractor(state):
    structured_llm = llm.with_structured_output(CandidateProfile)

    prompt = CANDIDATE_PROFILE_PROMPT.format(
        user_skills = ", ".join(state.get("user_skills", [])),
        resume_text = state.get("resume_text", "")
    )

    result = structured_llm.invoke(prompt)

    return {
        "candidate_profile": result
    }

def skill_gap_analyzer(state):
    structured_llm = llm.with_structured_output(SkillGap)

    prompt = SKILL_GAP_PROMPT.format(
        jd_analysis=state["jd_analysis"].model_dump_json(indent=2),
        candidate_profile=state["candidate_profile"].model_dump_json(indent=2)
    )

    result = structured_llm.invoke(prompt)
    return {"skill_gap": result}


def planner(state):
    structured_llm = llm.with_structured_output(PlanContext)

    prompt = PLANNER_PROMPT.format(
        skill_gap = state["skill_gap"].model_dump_json(indent=2),
        jd_analysis = state["jd_analysis"].model_dump_json(indent=2),
        prep_days = state["prep_days"]
    )

    result = structured_llm.invoke(prompt)

    return {
        "plan_context": result
    }


def roadmap_generator(state):
    structured_llm = google_llm.with_structured_output(Roadmap)

    prompt = ROADMAP_PROMPT.format(
        plan_context = state["plan_context"].model_dump_json(indent=2)
    )

    result = structured_llm.invoke(prompt)

    return {
        "roadmap": result
    }


def interview_topic_generator(state):
    structured_llm = llm.with_structured_output(InterviewTopics)

    prompt = INTERVIEW_TOPICS_PROMPT.format(
        plan_context = state["plan_context"].model_dump_json(indent=2)
    )

    result = structured_llm.invoke(prompt)

    return {
        "interview_topics": result.topics
    }


def project_recommender(state):
    structured_llm = llm.with_structured_output(ProjectSuggestions)

    prompt = PROJECT_RECOMMENDER_PROMPT.format(
        plan_context = state["plan_context"].model_dump_json(indent=2)
    )

    result = structured_llm.invoke(prompt)
    return {
        "project_suggestions": result.projects
    }


def resume_alignment_suggester(state):
    structured_llm = llm.with_structured_output(ResumeSuggestions)

    prompt = RESUME_ALIGNMENT_PROMPT.format(
        plan_context = state["plan_context"].model_dump_json(indent=2)
    )

    result = structured_llm.invoke(prompt)
    return {
        "resume_suggestions": result.suggestions
    }



def learning_resource_suggester(state):
    structured_llm = llm.with_structured_output(LearningResources)

    prompt = LEARNING_RESOURCES_PROMPT.format(
        plan_context = state["plan_context"].model_dump_json(indent=2)
    )

    result = structured_llm.invoke(prompt)
    return {
        "learning_resources": result.resources
    }


def merge_results(state):
    final = {
        "jd_analysis": state["jd_analysis"].model_dump(),
        "candidate_profile": state["candidate_profile"].model_dump(),
        "skill_gap": state["skill_gap"].model_dump(),
        "roadmap": state["roadmap"].model_dump(),

        "interview_topics": state["interview_topics"],
        "project_suggestions": state["project_suggestions"],
        "resume_suggestions": state["resume_suggestions"],
        "learning_resources": state["learning_resources"]
    }

    return {
        "final_response": final
    }

def response_formatter(state):
    # This can be used to format the final response if needed
    return {
        "final_response": state["final_response"]
    }