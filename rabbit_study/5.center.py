# coding=utf-8

import pika


class Center(object):
    def __init__(self):
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()
        # 定义接收返回消息的队列
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        self.response = body

    def request(self, n):
        self.response = None
        # 发送计算请求，并声明返回队列
        self.channel.basic_publish(
            exchange='',
            routing_key='compute_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue
            ),
            body=str(n)
        )
        while self.response in None:
            self.connection.process_data_events()
            return int(self.response)

center = Center()
print(" [x] Requesting increase(30)")
response = center.request(30)
print(" [.] Got %r" % (response,))