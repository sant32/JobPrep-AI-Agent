from app.graph.chains import (
    planner_chain,
    jd_extractor_chain,
    candidate_profile_chain,
    skill_gap_chain,
    roadmap_chain,
    interview_topics_chain,
    project_recommender_chain,
    resume_alignment_chain,
    learning_resources_chain,
    query_tavily_chain,
    project_validator_chain
)

from app.utils.tavily_search import tavily_search


def input_parser(state):
    return {
        "job_description": state["job_description"],
        "user_skills": state.get("user_skills", []),
        "resume_text": state.get("resume_text", ""),
        "prep_days": state.get("prep_days", 7)
    }

def JD_extractor(state):
    result = jd_extractor_chain.invoke(state["job_description"])

    return {
        "jd_analysis": result
    }



def candidate_profile_extractor(state):
    result = candidate_profile_chain.invoke({
        "user_skills": ", ".join(state.get("user_skills", [])),
        "resume_text": state.get("resume_text", "")
    })

    return {
        "candidate_profile": result
    }


def calculate_readiness_score(matched, partial, missing):
    total = len(matched) + len(partial) + len(missing)
    if total == 0:
        return 0

    score = (len(matched) * 1.0 + len(partial) * 0.5) / total
    return round(score * 100)





def skill_gap_analyzer(state):
    result = skill_gap_chain.invoke({
        "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        "candidate_profile": state["candidate_profile"].model_dump_json(indent=2)
    })

    calculate_score = calculate_readiness_score(
        matched=result.matched,
        partial=result.partial,
        missing=result.missing
    )

    result.readiness_score = calculate_score

    return {"skill_gap": result}



def planner(state):
    result = planner_chain.invoke({
        "skill_gap": state["skill_gap"].model_dump_json(indent=2),
        "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        "prep_days": state["prep_days"]
    })
    return {"plan_context": result}




def roadmap_generator(state):
    result = roadmap_chain.invoke({
        "plan_context": state["plan_context"].model_dump_json(indent=2),
        "prep_days": state["prep_days"]
    })

    return {
        "roadmap": result
    }



def interview_topic_generator(state):
    result = interview_topics_chain.invoke({
        "plan_context": state["plan_context"].model_dump_json(indent=2)
    })

    return {
        "interview_topics": result.topics
    }



def project_recommender(state):
    plan_context = state["plan_context"]

    retry_count = state.get("project_retry_count", 0)
    feedback = state.get("project_feedback", "")

    # 1. Generate search query
    query_obj = query_tavily_chain.invoke({
        "plan_context": plan_context.model_dump_json(indent=2)
    })

    query = query_obj.query
    search_results = tavily_search(query, max_results=5)

    # 2. Generate projects
    result = project_recommender_chain.invoke({
        "plan_context": plan_context.model_dump_json(indent=2),
        "search_results": search_results,
        "feedback": feedback
    })

    # 3. Validate generated projects
    validation = project_validator_chain.invoke({
        "plan_context": plan_context.model_dump_json(indent=2),
        "projects": result.projects
    })

    print("Project Validation Output:", validation.model_dump())
    return {
        "project_suggestions": result.projects,
        "project_score": validation.score,
        "project_feedback": validation.feedback,
        "project_retry_count": retry_count + 1
    }



def resume_alignment_suggester(state):
    print("state", state)
    result = resume_alignment_chain.invoke({
        "plan_context": state["plan_context"].model_dump_json(indent=2)
    })

    return {
        "resume_suggestions": result.suggestions
    }



def learning_resource_suggester(state):
    result = learning_resources_chain.invoke({
        "plan_context": state["plan_context"].model_dump_json(indent=2)
    })

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