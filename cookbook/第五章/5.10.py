"""
内存映射的二进制文件
"""

import os
import mmap
import os.path
import glob


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


##################path#################

path = '/Users/yz/Desktop' + "/thrift-0.11.0.tar.gz"
os.path.basename(path)
os.path.dirname(path)
os.path.join("tmp", "data", os.path.basename(path))
pat = '~/Data/data.csv'
os.path.expanduser(pat)
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)

# 获取文件元数据

os.path.getsize(path)  # 文件大小
os.path.getmtime(path)  # 文件的修改时间

# 获取文件列表
os.listdir(path)
os.chdir(path)


# 查找对应的文件

pyfiles = glob.glob("*.py")  # 这样会获取到当前目录所有的py文件
