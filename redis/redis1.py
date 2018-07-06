import redis

# 链接redis 加上decode_response=True 写入的键值对中的value为str类型，不加为字节类型
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# re = redis.StrictRedis(connection_pool=pool)

r.set('name', "zhangsan")

print(r['name'])
print(r.get('name'))
print(type(r.get("name")))

r.set('food', 'mutton', ex=3)
r.set('good', 'bcd', px=100000)
r.set('fruit', "abc", nx=True)  # 设置nx当good不存在的时候
print(r.get("good"))
print(r.set('fruit', 'watermelon', xx=True))  # xx 如果设置为True,
# 则只有name存在时，当前set操作才执行修改
r.setex('fruit2', "kkk", 300)  # 设置过期时间
print(r.get('fruit2'))
r.psetex('fruit3', 5000, "banana")  # psetex(name, time_ms, value)

r.mset(k1='v1', k2='v2')  # 一次存入多个值
print(r.mget("k1", "k2"))  # 一次去除多个值 返回列表

print(r.getset("fruit2", "orange"))  # 获取原来的值并设置新值
r.delete('name')

r.set("cn_name", "测试啊测试测啊")

print(r.getrange("cn_name", 0, 2))  # 取索引号是0-2 前3位的字节 君 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）

r.set("en_name", "wwww")
r.setrange('en_name', 1, "ccc")
r.setrange('en_name', 3, 'bbb')
r.append('en_name', 'eee')

print(r.get("en_name"))

source = "王八三"
for i in source:
    num = ord(i)
    print(num, bin(num))

print(r.getbit("en_name", 10))
print(r.bitcount('foo', 0, -1))
