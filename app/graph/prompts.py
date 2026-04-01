JD_EXTRACTOR_PROMPT = """
You are an expert technical recruiter.

Analyze the following job description and extract only the requested structured information.

Job Description:
{job_description}
"""

CANDIDATE_PROFILE_PROMPT = """
You are analyzing a candidate profile for a job preparation assistant.

User Skills:
{user_skills}

Resume Text:
{resume_text}

Extract only the requested structured profile information.
"""

SKILL_GAP_PROMPT = """
Compare the job requirements and candidate profile.

Job Analysis:
{jd_analysis}

Candidate Profile:
{candidate_profile}

Return only the requested structured comparison.
"""

PLANNER_PROMPT = """
You are building a preparation plan context for a job preparation assistant.

Skill Gap:
{skill_gap}

JD Analysis:
{jd_analysis}

Prep Days:
{prep_days}

Return only the requested structured plan context.
"""

ROADMAP_PROMPT = """
Create a personalized preparation roadmap.

Plan Context:
{plan_context}

Return a realistic roadmap for the candidate.

IMPORTANT:
- Include prep_days
- Include daily_plans
- Each daily plan must include:
  - day
  - title
  - focus
  - tasks

Return only structured output.
"""

INTERVIEW_TOPICS_PROMPT = """
Generate the most important interview preparation topics.

Plan Context:
{plan_context}
"""

PROJECT_RECOMMENDER_PROMPT = """
Suggest 3 portfolio projects aligned with the target role and skill gaps.

Plan Context:
{plan_context}
"""

RESUME_ALIGNMENT_PROMPT = """
Suggest resume alignment improvements based on the role and missing skills.

Plan Context:
{plan_context}
"""

LEARNING_RESOURCES_PROMPT = """
Suggest learning resources and study topics.

Plan Context:
{plan_context}
"""