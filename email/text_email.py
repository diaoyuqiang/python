from email.header import Header  # 对中文进行编码
from email.mime.text import MIMEText  # 邮件对象
from email.utils import parseaddr, formataddr  # 格式化邮箱
import smtplib  # 发送邮件

# 格式化邮箱（不格式化会被当做垃圾邮件）


def format_addr(s):
    name, addr = parseaddr(s)  # 比如：刁玉强<17853514421@163.com>
    return formataddr((Header(name, 'utf-8').encode('utf-8'), addr))


# 准备好数据
from_addr = '17853514421@163.com'  # 发件人
passworld = 'UZMFNFNXDTCPYDRZ'  # 授权码
smtp_server = 'smtp.163.com'  # 邮箱服务器地址
to_addr = input('收件人邮箱：')  # 收件人


# ---------------------构建邮件内容对象---------------------start----------
# 构建一个发送内容对象
msg = MIMEText("dyq发送的邮件", "plain", "utf-8")
# 标准邮件需要三个头部信息：From：发件人 To：收件人 Subject：标题
msg['From'] = format_addr(u'刁玉强<%s>' % from_addr)  # 发件人
to_name = input("收件人名称：")
msg['To'] = format_addr(u'{}<%s>'.format(to_name) % to_addr)  # 收件人
msg['Subject'] = Header(u'python学习资料', 'utf-8').encode('utf-8')  # 标题

# ---------------------构建邮件内容对象---------------------end----------


# ---------------------发送邮件---------------------start----------
# 创建一个发送邮件服务的对象
server = smtplib.SMTP(smtp_server, 25)  # 163邮箱的默认端口为
server.set_debuglevel(1)  # 是否显示发送日志 1|显示 2|不显示
server.login(from_addr, passworld)  # 登录邮箱
server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送邮件
server.quit()  # 关闭发送
# ---------------------发送邮件---------------------end----------