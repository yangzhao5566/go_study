from concurrent import futures
import time

"""
# futures.Executor 这是一个虚拟基类，提供了异步执行的方法
# submit(function, argument): 调度函数（可调用的对象）的执行，将 argument 作为参数传入。
# map(function, argument): 将 argument 作为参数执行函数，以 异步 的方式。
# shutdown(Wait=True): 发出让执行者释放所有资源的信号。
# concurrent.futures.Future: 其中包括函数的异步执行。Future对象是submit任务（即带有参数的functions）到executor的实例。
"""

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def count(number):
    for i in range(10000000):
        i += 1
    return i * number


def evaluate_item(x):
    result_item = count(x)
    return result_item


if __name__ == "__main__":
    start_time = time.time()
    for item in number_list:
        print(evaluate_item(item))
    print("Sequential execution in " + str(time.time() - start_time), "seconds")

    start_time_1 = time.time()
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        future = [executor.submit(evaluate_item, item) for item in number_list]
        for futu in futures.as_completed(future):
            print(futu.result())
    print("Thread pool execution in " + str(time.time() - start_time_1),
          "seconds")

    start_time_2 = time.time()
    with futures.ProcessPoolExecutor(max_workers=5) as executor:
        future = [executor.submit(evaluate_item, item) for item in number_list]
        for futus in futures.as_completed(future):
            print(futus.result())
    print("Process pool execution in " + str(time.time() - start_time_2), "seconds")

