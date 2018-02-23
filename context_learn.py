class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Begin")
        return self
    
    def __exit__(self, exc_type, exc_value, tracback):
        if exc_type:
           print("Error")
        else:
            print("End")

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()

# 可以用一下方式代替
from contextlib import contextmanager

class Query2(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print("begin")
    q = Query2(name)
    yield q
    print("End")

# 通过yield 的方式将with ... as var 的内容传入contextmanager中 进行处理

with create_query("Bob2") as b:
    b.query()

# 在某段代码执行前后自动增加一段代码

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>

# 如果一个对象没有实现上下文，就不能用with来打开但是可以用closing来实现

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen("https://www.baidu.com")) as page:
    for line in page:
        print(line)

