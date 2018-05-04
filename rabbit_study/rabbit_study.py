# coding = utf-8

# pika  rabbitmq python库

import pika

# 链接服务器

# 用户名密码登录用 user_pwd = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')  # 本地链接用这个
)

channel = connection.channel()

"""
声明消息队列，消息将在这个队列中进行传递。如果将消息发送到不存在的队列，
rabbitmq将会自动清除这些消息。
"""
channel.queue_declare(queue='hello')
#####################持久化#####################
"""
消息持久化 ：
channel.queue_declare(queue='hello', durable=True)
因为rabbit不支持对一个已经存在的队列设置两个模式所以会报错

发送任务时，用delivery_mode =2 来标记任务为持久化存储

channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
"""

"""
发送消息到上面的hello队列，其中exchange表示交换器，能精确指定消息应该发送到哪个队列，
routing_key设置为队列的名称，body就是发送的内容，具体发送细节暂时先不关注
"""

channel.basic_publish(exchange='', routing_key='hello', body='Hello World')

# connection.close()


def callback(ch, method, properties, body):
    """

    :param ch: 用来消息确认
    :param method:
    :param properties:
    :param body:
    :return:
    """
    print(" [x] Received %r" % (body,))
    ch.basic_ack(delivery_tag=method.delivery_tag) # 进行消息确认


channel.basic_consume(callback, queue='hello', no_ack=True)

"""
channel.basic_consume(callback, queue='hello', no_ack=False)  
用这个代码运行，即使其中一个工作者ctrl+c退出后，正在执行的任务也不会丢失，
rabbitmq会将任务重新分配给其他工作者
"""
channel.start_consuming()

connection.close()


#####################公平调度###############
"""
即当一个工作者完成当前的任务后再给其分配任务
使用参数为：
channel.basic_qos(prefetch_count=1)
"""
