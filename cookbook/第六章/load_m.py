"""
通过钩子远程加载模块
"""

import imp
import urllib.request
import sys


def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode("utf-8")
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, "exec")
    mod.__file__ = url
    mod.__package__ = ""
    exec(code, mod.__dict__)
    return mod


