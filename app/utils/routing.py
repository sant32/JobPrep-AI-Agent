


def project_route(state):
    score = state.get("project_score", 0)
    retry_count = state.get("project_retry_count", 0)

    if score >= 7:
        return "merge_results"
    
    if retry_count >= 3:
        return "merge_results"
    
    return "project_recommender" 