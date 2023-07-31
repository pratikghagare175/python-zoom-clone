from fastapi import FastAPI;
from app.routes.user_route import router as user_router
app = FastAPI();

@app.get("/_healthz")
async def health_check():
    return {"ok":True}

app.include_router(user_router)