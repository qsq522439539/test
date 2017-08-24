#!/usr/bin/env python
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#发送邮箱服务器
smtpserver = 'smtp.163.com'
#发送邮箱用户密码
user = '13278231466@163.com'
password = 'xxxxxxxxxxxxxxxxx'

#发送邮箱
sender = '13278231466@163.com'
#接收邮箱
receiver = 'qinshiqiang@baicells.com'
#邮件主题
subject = 'Python email test'
#正文
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'qsq<13278231466@163.com>'
msg['To'] = "qinshiqiang@baicells.com"

#加附件
sendfile = open('C:\\Users\\admin\\Desktop\\11.txt','rb').read()
att = MIMEText(sendfile,'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename = 11.txt'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = 'qsq<13278231466@163.com>'
msgRoot['To'] = "qinshiqiang@baicells.com"
msgRoot.attach(att)
msgRoot.attach(msg)


if __name__ == "__main__" :
	#发送邮件
	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(user,password)
	smtp.sendmail(sender, receiver, msgRoot.as_string())
	smtp.quit()