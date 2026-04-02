from pydantic import BaseModel, Field
from typing import List, Optional


# ---- JD ANALYSIS ---- 

class JDAnalysis(BaseModel):
    role: str
    seniority: str
    domain: str
    required_skills: List[str]
    preferred_skills: List[str]
    responsibilities: List[str]
    tools_frameworks: List[str]



# ---- CANDIDATE PROFILE ----
class CandidateProfile(BaseModel):
    known_skills: List[str]
    projects: List[str]
    strengths: List[str]
    experience_level: str



# ---- SKILL GAP ----
class SkillGap(BaseModel):
    matched: list[str]
    partial: list[str]
    missing: list[str]
    priority_order: list[str]
    readiness_score: int = Field(..., ge=0, le=100)  # Score between 0 and 100


#  ---- PLANNER ----
class PlanContext(BaseModel):
    target_role: str
    prep_days: int
    must_focus: List[str]
    matched_skills: List[str]
    missing_skills: List[str]
    output_modules: List[str]


# ---- ROADMAP ----
class DailyPlanItem(BaseModel):
    day: int = Field(..., description="Day number in the preparation roadmap, starting from 1")
    title: str = Field(..., description="Short descriptive title for the day's study plan")
    focus: str = Field(..., description="Main concept or skill to focus on for the day")
    tasks: List[str] = Field(..., description="List of actionable study or project tasks for the day")


class Roadmap(BaseModel):
    prep_days: int = Field(..., description="Total number of preparation days")
    daily_plan: List[DailyPlanItem] = Field(
        ...,
        description="List of daily preparation plans, one item per day"
    )

class InterviewTopics(BaseModel):
    topics: List[str]


class ProjectSuggestion(BaseModel):
    title: str
    level: str
    why_it_matters: str
    stack: List[str]


class ProjectSuggestions(BaseModel):
    projects: List[ProjectSuggestion]


class ResumeSuggestions(BaseModel):
    suggestions: List[str]


class LearningResource(BaseModel):
    topic: str
    type: str
    why: str


class LearningResources(BaseModel):
    resources: List[LearningResource]