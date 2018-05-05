# coding=utf-8

import pika

"""
设定交换机的类型（type）为direct。上一篇是设置为fanout，
表示广播的意思，会将消息发送到所有接收端，这里设置为direct表示要根据设定的路由键来发送消息。
发送信息时设置发送的路由键。
"""

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

routings = ['info', 'warning', 'error']
channel.exchange_declare(exchange='messages', exchange_type='direct')

for routing in routings:
    message = '%s message.' % routing
    channel.basic_publish(exchange='messages', routing_key=routing,
                          body=message)
    print(message)

connection.close()
