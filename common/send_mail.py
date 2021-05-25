# coding:utf-8
import smtplib,os,sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.logger import log
from config.allpath import reprort_path


Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
# 测试报告的路径
reportPath = reprort_path
log = log()
# 配置收发件人
recvaddress = ['18599936472@163.com',]
# 163的用户名和密码
sendaddr_name = '18599936472@163.com'
sendaddr_pswd = 'WERJPHVUZCUVWYHG'


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '测试报告主题'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        self.email_text = '自动化测试报告'
        self.part_text = MIMEText(self.email_text)
        self.msg.attach(self.part_text)

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('smtp.163.com', 25)
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            log.info("发送邮件成功")
            smtp.close()
        except:
            log.error('发送邮件失败')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()