import redis
import dramatiq
from dramatiq_abort import backends, Abortable

redis_client = redis.Redis.from_url("redis://localhost:6379/0")
abortable = Abortable(
    backend=backends.RedisBackend(client=redis_client)
)
dramatiq.get_broker().add_middleware(abortable)

@dramatiq.actor
def test_abort_job(message):
    print(message)
    return None
