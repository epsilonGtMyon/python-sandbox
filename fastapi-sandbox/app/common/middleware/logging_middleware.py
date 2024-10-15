import logging
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:
        url = request.url
        logger.info("%s begin", url)
        response = await call_next(request)
        logger.info("%s end", url)
        return response
