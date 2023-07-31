from redis import Redis
from app.config.logger_config import logger

redis_client = Redis(host="localhost",port=6379)

if redis_client:
    logger.info("== Redis Connected ==");
else:
    logger.error("== Error in Connecting Redis ==")