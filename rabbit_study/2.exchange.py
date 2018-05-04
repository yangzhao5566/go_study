# coding=utf-8

"""
exchange 类型有四种：
    direct ： 相当于单点广播
    fanout ： 相当于多播，即所有的worker都能收到消息
    topic ： 匹配广播
    headers
"""

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# 定义交换机
channel.exchange_declare(exchange='message', type='fanout')

# 生成随机队列， 并绑定到交换机上
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='messages', queue=queue_name)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))


channel.basic_consume(callback, queue=queue_name, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()

