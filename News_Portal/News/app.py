import redis
from apscheduler.jobstores.redis import RedisJobStore

red = redis.Redis(
    host='redis-10634.c328.europe-west3-1.gce.redns.redis-cloud.com',
    port=10634,
    password='wkz9qv20I2FPACoLh71J33fZs0ww3dJH'
)
