"""
创建临时文件和文件夹
https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p19_make_temporary_files_and_directories.html
"""

from tempfile import TemporaryFile

with TemporaryFile("w+t") as f:
    f.write("hello world\n")
    f.write("Testing\n")
    f.seek(0)
    data = f.read()


