from fastapi import APIRouter
from app.schemas.request import JobPrepRequest
from app.schemas.response import FinalJobResponse
from app.graph.builder import build_graph


router = APIRouter()

graph = build_graph()

@router.post("/analyze-job", response_model=FinalJobResponse)
def analyze_job(request: JobPrepRequest):
    result = graph.invoke({
        "job_description": request.job_description,
        "user_skills": request.user_skills,
        "resume_text": request.resume_text,
        "prep_days": request.prep_days
    })

    return result.get("final_response", {})

