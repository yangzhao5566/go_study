# coding-utf-8

import pika
import sys

# http://www.01happy.com/python-rabbitmq-routing-patten/
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='messages', exchange_type='topic')

routings = sys.argv[1:]

if not routings:
    print(sys.stderr, "Usage: %s [routing_key]..." % (sys.argv[0],))
    exit()

# 生成临时队列，并绑定到交换机上，设置路由键
result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

for routing in routings:
    channel.queue_bind(exchange='messages', queue=queue_name,
                       routing_key=routing)

"""
进行模糊匹配的关键是对routing_name 来进行匹配　
"""

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))

channel.basic_consume(callable, queue=queue_name, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
