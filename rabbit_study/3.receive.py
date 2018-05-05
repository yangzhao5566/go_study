# coding=utf-8

import pika
import sys
"""
设定交换机的类型（type）为direct。
增加命令行获取参数功能，参数即为路由键。
将队列绑定到交换机上时，设定路由键。
"""
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='messages', exchange_type='direct')

routings = sys.argv[1:]

if not routings:
    routings = ['info']

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

for routing in routings:
    channel.queue_bind(
        exchange='messages',
        queue=queue_name,
        routing_key=routing
    )


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))

channel.basic_consume(callback, queue=queue_name, no_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()