# coding=utf-8

import pika
import threading
import uuid

"""
使用python的uuid来产生唯一的correlation_id。
发送计算请求时，设定参数correlation_id。
定义一个字典来保存返回的数据，并且键值为相应线程产生的correlation_id。
"""


class MyThread(threading.Thread):
    def __init__(self, func, num):
        super(MyThread, self).__init__()
        self.func = func
        self.num = num

    def run(self):
        print(" [x] Requesting increase(%d)" % self.num)
        response = self.func(self.num)
        print(" [.] increase(%d)=%d" % (self.num, response))


class Center(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))

        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            self.on_response,
            no_ack=True,
            queue=self.callback_queue
        )
        self.response = {}

    def on_response(self, ch, method, props, body):
        self.response[props.correlation_id] = body

    def request(self, n):
        corr_id = str(uuid.uuid4())
        self.response[corr_id] = None
        self.channel.basic_publish(
            exchange='',
            routing_key='compute_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=corr_id,
            ),
            body=str(n)
        )

        while self.response[corr_id] is None:
            self.connection.process_data_events()
        return int(self.response[corr_id])

center = Center()

# 发起5次计算请求
nums= [10, 20, 30, 40, 50]
threads = []
for num in nums:
    threads.append(MyThread(center.request, num))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

