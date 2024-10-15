import logging
import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)

class ProcesstimeMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        # yieldがあるとその分は含まれない
        process_time = time.perf_counter() - start_time
        logger.info("%s %s", request.url, process_time)
        return response
