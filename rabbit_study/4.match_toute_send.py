# coding=utf-8

import pika
"""
模糊匹配　交换机的类型为topic

路由键的工作原理：每个接收端的消息队列在绑定交换机的时候，可以设定相应的路由键。
发送端通过交换机发送信息时，可以指明路由键 ，交换机会根据路由键把消息发送到相应的消息队列，
这样接收端就能接收到消息了。
"""

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()


#　定义交换机，设置类型为topic
channel.exchange_declare(exchange='messages', exchange_type='topic')

routings = ['happy.work', 'happy.life', 'sad.work', 'sad.life']


# 将消息依次发送到交换机，并设定路由键
for routing in routings:
    message = '%s message.' % routing
    channel.basic_publish(
        exchange='messages',
        routing_key=routing,
        body=message
    )
    print(message)

connection.close()
