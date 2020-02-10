import redis
import os

assert os.getenv('REDIS_HOST', '0.0.0.0:6379')
pool = redis.ConnectionPool(host=os.getenv('REDIS_HOST'), port=6379, db=3, password=123456)

client = redis.Redis(connection_pool=pool)

# 50min
EXPIRE_TIME = 60 * 50


class RedisClient:

    @staticmethod
    def set_dict(name, dic, time=EXPIRE_TIME):
        if name and dic:
            client.hmset(name=name, mapping=dic)
            client.expire(name, time=time)

    @staticmethod
    def get_dict(name):
        if not name:
            return {}
        data = client.hgetall(name)
        if data:
            return {k.decode('U8'): v.decode('U8') for k, v in data.items()}
        return {}

    @staticmethod
    def set_nx_ex(name, value):
        """
        :param name:
        :param value:
        :return:
        """
        if client.set(name=name, value=value, ex=5 * 60, nx=True):
            return True
        return False

    @staticmethod
    def del_key(name):
        if name:
            client.delete(name)


if __name__ == '__main__':
    RedisClient.set_dict('user:1', {
        'name': "李数龙",
        'age': 21,
    })

    RedisClient.set_dict('user:1', {
        'age': 22,
        'address': "北京"
    })
    print(RedisClient.get_dict("user:1"))

    RedisClient.del_key('user:1')

    print(RedisClient.get_dict("user:1"))
