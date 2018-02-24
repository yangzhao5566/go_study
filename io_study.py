# 内存中读写文件 BytesIO  和 StringIO
# https://www.kancloud.cn/thinkphp/python-guide/39358

from io import StringIO
f = StringIO() # 先创建一个StringIO 对象 然后像文件一样写入
f.write("hello")
print(f.getvalue())

# 读取StringIO 
f = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())


# BytesIO 二进制流读写文件
#  写入的不是str，而是经过UTF-8编码的bytes。

from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
