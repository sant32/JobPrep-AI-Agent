from langgraph.graph import StateGraph, START, END
from app.graph.state import AgentState
from app.graph.nodes import (
    input_parser,
    JD_extractor,
    candidate_profile_extractor,
    skill_gap_analyzer,
    planner,
    roadmap_generator,
    interview_topic_generator,
    project_recommender,
    resume_alignment_suggester,
    learning_resource_suggester,
    merge_results,
    response_formatter
)


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("input_parser", input_parser)
    graph.add_node("jd_extractor", JD_extractor)
    graph.add_node("candidate_profile_extractor", candidate_profile_extractor)
    graph.add_node("skill_gap_analyzer", skill_gap_analyzer)
    graph.add_node("planner", planner)

    graph.add_node("roadmap_generator", roadmap_generator)
    graph.add_node("interview_topic_generator", interview_topic_generator)
    graph.add_node("project_recommender", project_recommender)
    graph.add_node("resume_alignment_suggester", resume_alignment_suggester)
    graph.add_node("learning_resource_suggester", learning_resource_suggester)

    graph.add_node("merge_results", merge_results)
    graph.add_node("response_formatter", response_formatter)

    graph.add_edge(START, "input_parser")
    graph.add_edge("input_parser", "jd_extractor")
    graph.add_edge("jd_extractor", "candidate_profile_extractor")
    graph.add_edge("candidate_profile_extractor", "skill_gap_analyzer")
    graph.add_edge("skill_gap_analyzer", "planner")


    # Parallel fan-out 
    graph.add_edge("planner", "roadmap_generator")
    graph.add_edge("planner", "interview_topic_generator")
    graph.add_edge("planner", "project_recommender")
    graph.add_edge("planner", "resume_alignment_suggester")
    graph.add_edge("planner", "learning_resource_suggester")

    # Fan-in
    graph.add_edge("roadmap_generator", "merge_results")
    graph.add_edge("interview_topic_generator", "merge_results")
    graph.add_edge("project_recommender", "merge_results")
    graph.add_edge("resume_alignment_suggester", "merge_results")
    graph.add_edge("learning_resource_suggester", "merge_results")

    graph.add_edge("merge_results", "response_formatter")
    graph.add_edge("response_formatter", END)

    return graph.compile()
