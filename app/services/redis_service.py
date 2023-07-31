from app.config.redis_config import redis_client

class RedisService:
    def __init__(self):
      self
      
    async def redisSet(self,key,value):
      return redis_client.set(key,value)