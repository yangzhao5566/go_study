"""
增加或改变已打开文件的编码
"""

import urllib.request
import io

u = urllib.request.urlopen("www.baidu.com")
f = io.TextIOWrapper(u, encoding="utf-8")
text = f.read()

