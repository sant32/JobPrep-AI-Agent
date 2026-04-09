from langchain_core.prompts import ChatPromptTemplate


JD_EXTRACTOR_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert technical recruiter."),
    ("human", """Analyze the following job description and extract only the requested structured information.
Job Description:
{job_description}""")

])

CANDIDATE_PROFILE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are analyzing a candidate profile for a job preparation assistant."),
    ("human", """Extract only the requested structured profile information.
User Skills:
{user_skills}
     
Resume Text:
{resume_text}
""")
])




SKILL_GAP_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career preparation planner."),
    ("human", """Compare the job requirements and candidate profile.
Rules:
- Put clearly strong skills in matched.
- Put partially demonstrated but not fully proven skills in partial.
- Put genuinely absent or weakly demonstrated skills in missing.
- priority_order must prioritize:
  1. missing skills first
  2. then partial skills
  3. do NOT prioritize already strong matched skills unless they are core for interview depth   
Return concise, practical output.
     
Job Analysis:
{jd_analysis}
     
Candidate Profile:  
{candidate_profile}
""")
])




PLANNER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career preparation planner."),
    ("human", """
Skill gap:
{skill_gap}

JD analysis:
{jd_analysis}

Prep days:
{prep_days}

Create a preparation plan context.
""")
])




ROADMAP_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career preparation planner."),
    ("human", """Create a personalized preparation roadmap.
Rules:
- Focus mostly on missing and partial skills.
- Do NOT waste days on skills the user already strongly knows.
- Make the roadmap practical and interview-oriented.
- Include implementation tasks, not just theory.
- Tailor the plan to the target role.
- Return exactly {prep_days} days.  
     
Plan Context:
{plan_context}
""")
])



INTERVIEW_TOPICS_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career preparation planner."),
    ("human", """Generate the most important interview preparation topics.
Rules:
- Return only 8 to 12 topics.
- Focus on high-value technical interview areas.
- Avoid generic items like "Introduction to AI" or "Mock Interview".
- Prioritize missing skills, partial skills, and likely interview discussion areas.
     
Plan Context:
{plan_context}
""")
])



PROJECT_RECOMMENDER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert Career Coach.

Instructions:
1. Suggest 3 projects based on the Search Results.
2. **CRITICAL:** If a specific GitHub URL is found in the search results, use it. 
3. If NO specific URL is found, set the "url" field to "N/A - Search for similar repos on GitHub". 
4. DO NOT invent fake URLs like "github.com/example".
5. Focus on technologies mentioned in the Job Description: GraphQL, AWS, Security, Python/Node.js.
"""),
    ("human", """
Search Results:
{search_results}

Candidate Profile:
{plan_context}

Generate project suggestions.
""")
])



RESUME_ALIGNMENT_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career preparation planner."),
    ("human", """Suggest concise resume improvements based on the target role and missing skills.
     
Rules:
- Return 5 to 8 suggestions only.
- Each suggestion should be short, practical, and resume-actionable.
- Avoid long explanations or essay-style output.
     
Plan Context:
{plan_context}
""")
])



LEARNING_RESOURCES_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career preparation planner."),
    ("human", """Suggest learning resources and study topics.
Rules:
- Focus mainly on missing and partial skills.
- Return 5 to 8 resources only.
- Prefer practical implementation-oriented recommendations.
- Avoid generic filler.
     
Plan Context:
{plan_context}
""")
])




LEARNING_RESOURCES_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career preparation planner."),
    ("human", """Suggest learning resources and study topics.
Rules:
- Focus mainly on missing and partial skills.
- Return 5 to 8 resources only.
- Prefer practical implementation-oriented recommendations.
- Avoid generic filler.
     
Plan Context:
{plan_context}
""")
])




TAVILY_SEARCH_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert at generating highly effective web search queries for developers.

Your goal:
Generate a precise, high-quality search query to retrieve:
- Real-world projects
- GitHub repositories
- Practical implementations

Guidelines:
- Include role and technical context
- Include specific technologies (skills)
- Prefer terms like: "real-world", "production", "backend", "project", "GitHub"
- Avoid vague or generic queries
- Keep it concise (max 15-20 words)
- Focus on practical and implementable results
"""),
    ("human", """
Plan Context:
{plan_context}

Generate a search query based on:
- Target role
- Missing skills (priority)
- Existing skills (secondary)
""")
])



PROJECT_VALIDATOR_PROMPT = ChatPromptTemplate.from_messages([
    
    ("system", """
You are a senior technical hiring mentor and project evaluator.

Your task is to evaluate project suggestions for a candidate preparing for job interviews.

You will be given:
1. Candidate plan context
2. Generated project suggestions

Evaluate the projects strictly based on:

1. Relevance to the target job role
2. Alignment with the job description
3. Coverage of candidate skill gaps
4. Resume impact
5. Interview usefulness
6. Practical feasibility
7. Uniqueness (avoid generic beginner projects)
8. Technical depth (backend / APIs / deployment / architecture / AI workflows if relevant)

Scoring Rules:
- 9 to 10 = excellent, highly relevant, resume-worthy
- 7 to 8.9 = good and acceptable
- 5 to 6.9 = average, needs improvement
- below 5 = poor, should regenerate

Return:
- score = numeric score from 1 to 10
- feedback = concise explanation of what is weak or strong in the projects
"""),
    ("human", """
Candidate Plan Context:
{plan_context}

Generated Projects:
{projects}
""")
])