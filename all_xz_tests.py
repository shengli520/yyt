# coding=utf-8
import unittest
import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from BeautifulReport import BeautifulReport

# -------定义：取最新测试报告----------
#
# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
casepath = os.path.join(curpath, "xz_test_case")
print(casepath)
# if not os.path.exists(casepath):
#     print("测试用例需放到‘case’文件目录下")
#     os.mkdir(casepath)
reportpath = os.path.join(curpath, "report/test_result/xz_result")
print(reportpath)
#if not os.path.exists(reportpath): os.mkdir(reportpath)

now = time.strftime('%Y-%m-%d_%H_%M_%S_')


def new_file(test_dir):
    lists = os.listdir(test_dir)
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    file_path = os.path.join(test_dir, lists[-1])
    return file_path


def send_email(newfile):
    f = open(newfile, 'rb')
    mail_body = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱用户名/密码
    user = 'a50404580@163.com'
    password = 'zsl123456'

    # 发送邮箱
    sender = 'a50404580@163.com'

    # 多个接收邮箱
   # receiver = ['a50404580@163.com','sheng5202341314@qq.com','shengli.zheng@eascs.com',"cathy.xiong@eascs.com"]
    receiver = ['a50404580@163.com',
                'sheng5202341314@qq.com', 'shengli.zheng@eascs.com']
    # receiver=['sheng5202341314@qq.com','shengli.zheng@eascs.com',"cathy.xiong@eascs.com",'yao.liu@eascs.com','chunhua.luo@eascs.com']

    # 发送邮件主题
    subject = '这是一封善良的自动化测试报告'

    # 编写 HTML类型的邮件正文
#    msg = MIMEText(mail_body,'html','utf-8')

    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    # 要在163有限设置授权码（即客户端的密码），否则会报535
    msg['From'] = 'a50404580@163.com '

    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def add_case(case_path=casepath, rule="xzx*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='test_result/xz_result' + '\\' + now +
                  'report.html', description='测试deafult报告', log_path='report')

if __name__ == '__main__':
    # test_dir = "/selenium-py/xz_test_case/"
    # test_report = "/selenium-py/test_result/xz_result"

    #discover=unittest.defaultTestLoader.discover(test_dir, pattern='xz*.py')
    # now=time.strftime('%Y-%m-%d_%H_%M_%S_')
    # filename = test_report+'\\'+ now + 'result.html'
    # fp=open(filename ,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u"OA-vue正式环境菜单查询报告",
    #     description=u"环境：Window 7  浏览器：Chrome")
    # runner.run(discover)
    # fp.close()
    cases = add_case()
    run(cases)
    new_report = new_file(reportpath)
    send_email(new_report)
