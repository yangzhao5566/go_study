# coding=utf-8

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='messages', type='fanout')

channel.basic_publish(exchange='messages', routing_key='', body='Hello World')
print(" [x] Sent 'Hello World!'")


"""
basic_publish方法的参数exchange被设定为相应交换机，因为是要广播出去，发送到所有队列，
所以routing_key就不需要设定了。
exchange如果为空，表示是使用匿名的交换机，在上面交换机信息的图片中可以看到有amq.*
这样的交换机，就是系统默认的交换机了。routing_key在使用匿名交换机的时候才需要指定，
表示发送到哪个队列的意思。第一篇的例子演示了这个功能。
"""
connection.close()