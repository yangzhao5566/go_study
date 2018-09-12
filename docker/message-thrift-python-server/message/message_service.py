"""
MessageService
"""
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from api import MessageService


sender = "imooc@163.com"
authCode = "aA111111"


class MessageServiceHandler(object):
    def sendMobileMessage(self, mobile, message):
        """
        Parameters:
         - mobile
         - message
        """
        print("sendMobileMessage:mobile:%s, message:%s"%(mobile, message))
        return True

    def sendEmailMessage(self, email, message):
        """
        Parameters:
         - email
         - message
        """
        print("sendEmailMessage email:%s, message:%s"%(email, message))
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj["From"] = sender
        messageObj["to"] = email
        messageObj["Subject"] = Header("慕课网邮件", "utf-8")
        smtpObj = smtplib.SMTP("smtp.163.com")
        smtpObj.login(sender, authCode)
        smtpObj.sendmail(sender, [email], messageObj.as_string())
        print("send email success")
        return True


if __name__ == "__main__":
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9090")
    tfactory = TTransport.TFramedTransportFactory()  # 帧传输
    pfactory = TBinaryProtocol.TBinaryProtocolFactory() # 二进制传输协议

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thirft server start")
    server.serve()
    print("python thirft server exit")

