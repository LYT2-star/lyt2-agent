# apps/api/utils/limiter.py

from fastapi import Request, HTTPException
from time import time

user_last_request_time = {}

def rate_limit(request: Request, min_interval: float = 2.0):
    ip = request.client.host
    now = time()
    last_time = user_last_request_time.get(ip, 0)
    if now - last_time < min_interval:
        raise HTTPException(status_code=429, detail="请求过于频繁")
    user_last_request_time[ip] = now

