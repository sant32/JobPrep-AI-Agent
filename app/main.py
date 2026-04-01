from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="JobPrep AI Agent", description="An AI agent to help job seekers prepare for their interviews by analyzing job descriptions and providing personalized recommendations.", version="1.0.0")

@app.get("/")
async def deff():
    return {"message": "Holle"}
 

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", debug=True)