"""
user server
"""

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from .user import UserService

from .usermodel import session, User


class UserInfo(object):
    def getUserById(self, id):
        """
        Parameters:
         - id
        """
        result = session.query(User.username, User.email, User.mobile,
                               User.password, User.id).filter(
            User.id == id).all()
        print(result)
        result = [dict(one) for one in result]
        return result

    def getUserByName(self, username):
        """
        Parameters:
         - username
        """
        result = session.query(User.username, User.email, User.mobile,
                           User.password, User.id).filter(User.username ==
                                                          username).all()
        result = [dict(one) for one in result]
        return result

    def registerUser(self, userInfo):
        """
        Parameters:
         - userInfo
        """
        newUser = User(**userInfo)
        session.add(newUser)
        session.commit()


if __name__ == "__main__":
    handler = User()
    processor = UserService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9091")
    tfactory = TTransport.TFramedTransportFactory()  # 帧传输
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()   # 二进制传输协议
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python user server start")
    server.serve()
