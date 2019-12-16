#_*_coding:utf-8_*_
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 处理多种形态的邮件主体我们需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
# 处理图片需要 MIMEImage 类
# from email.mime.image import MIMEImage

# 设置服务器所需信息
fromaddr = '2524165845@qq.com'  # 邮件发送方邮箱地址
password = 'ixawrvaarsykdjed'  # 密码(部分邮箱为授权码)
toaddrs = ['deancsdfy@163.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

#创建一个带附件的实例
msg = MIMEMultipart()
#构造附件
file = MIMEText(open('report\HTMLREport.html','rb').read(),'base64','utf-8')
file["Content-Disposition"] = 'attachment; filename="测试报告"' #这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(file)

# 设置email信息
# ---------------------------发送字符串的邮件-----------------------------
# 邮件内容设置
msg = MIMEText('测试报告', 'plain', 'utf-8')
# 邮件主题
msg['Subject'] = '自动化测试报告'
# 发送方信息
msg['From'] = fromaddr
# 接受方信息
msg['To'] = toaddrs[0]
# ---------------------------------------------------------------------



# 登录并发送邮件
try:
    server = smtplib.SMTP_SSL('smtp.qq.com',465)  # 163邮箱服务器地址，端口默认为25
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

except smtplib.SMTPException as e:
    print('error', e)  # 打印错误
