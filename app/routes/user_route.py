from fastapi import APIRouter
from pydantic import BaseModel
from app.services.redis_service import RedisService

router = APIRouter()
redisConfig = RedisService()
class SetBody(BaseModel):
    cache_key:str
    value:str

@router.post("/test/set")
async def set_test(body:SetBody):
    result = await redisConfig.redisSet(body.cache_key,body.value)
    return {"success":True, "data":result}