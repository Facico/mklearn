from email.mime.text import MIMEText
import smtplib
import time
msg=MIMEText('Hello , you are sb','plain','utf-8')
from_addr='Facico19807609219@163.com'
password='lashibudaizhi'
to_addr='845161327@qq.com'
HOST = 'smtp.163.com'
PORT='25'
"""from_addr=input('From:')
password=input('Password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()"""
smtp_obj=smtplib.SMTP()
bz=1
#while bz:
  #  try:
smtp_obj.connect(host=HOST,port=PORT)
  #  except NewConnectionError:
 #       print("HTTP请求失败！！！正在重发...")
  #  else：
  #      bz=0
   # time.sleep(2)
res=smtp_obj.login(user=from_addr,password=password)
print('login result: ',res)