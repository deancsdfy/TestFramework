#_*_coding:utf-8_*_
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
from framework.logger import Logger

logger = Logger('log').getlogger()
def sendTestReportEmail():
    # 设置服务器所需信息
    fromaddr = '2524165845@qq.com'  # 邮件发送方邮箱地址
    password = 'ixawrvaarsykdjed'  # 密码(部分邮箱为授权码)
    toaddrs = ['deancsdfy@163.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    
    # 读取测试报告内容
    with open('report\HtmlReport.html','rb') as f:
        content = f.read()
    
    # 邮件内容设置，邮件正文以HTML解析展示
    msg = MIMEText(content, 'HTML', 'utf-8')
    # 邮件主题
    msg['Subject'] = '自动化测试报告'
    # 发送方信息
    msg['From'] = fromaddr
    # 接受方信息
    msg['To'] = toaddrs[0]
    
    # 登录并发送邮件
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com',465)  # 163邮箱服务器地址，端口默认为25
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        logger.info('邮件发送成功')
        server.quit()
    
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
