"""
argparse model study
"""

import argparse


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", type=str, help="主机",
                        default="localhost")
    parser.add_argument("-p", "--port", type=int, help="端口", default=27017)
    parser.add_argument("-d", "--database", type=str,
                        help="数据库", default="default")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = args_parse()
    print(args.host, args.port, args.database)
