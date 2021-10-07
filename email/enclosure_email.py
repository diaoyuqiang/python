from email.header import Header  # 对中文进行编码
from email.mime.text import MIMEText  # 邮件对象
from email.utils import parseaddr, formataddr  # 格式化邮箱
import smtplib  # 发送邮件
# 附件对象使用的模块
from email import encoders  # 编码
from email.mime.base import MIMEBase  # base64解析
from email.mime.multipart import MIMEMultipart  # 请求头信息

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
# 创建附件对象


msg = MIMEMultipart()
# add MIMEText
msg.attach(MIMEText('这是一个有附件的邮件', 'plain', 'utf-8'))  # 文件内容
# add file
with open('reborn.jpg', 'rb') as f:

    # 设置附件的MIME和文件名以及类型
    mime = MIMEBase('image', 'jpg', filename='reborn.jpg')
    # 加上必须的请求头信息
    mime.add_header('Content-Disposition', 'attachment', filename='reborn.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

# 标准邮件需要三个头部信息：From：发件人 To：收件人 Subject：标题
msg['From'] = format_addr(u'刁玉强<%s>' % from_addr)  # 发件人
to_name = input("收件人名称：")
msg['To'] = format_addr(u'{}<%s>'.format(to_name) % to_addr)  # 收件人
msg['Subject'] = Header(u'python学习资料', 'utf-8').encode('utf-8')  # 标题

# ---------------------构建邮件内容对象---------------------end----------


# ---------------------发送邮件---------------------start----------
# 创建一个发送邮件服务的对象
server = smtplib.SMTP(smtp_server, 25)  # 163邮箱的默认端口为
# server.set_debuglevel(1)  # 是否显示发送日志 1|显示 2|不显示
server.login(from_addr, passworld)  # 登录邮箱
server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送邮件
server.quit()  # 关闭发送
# ---------------------发送邮件---------------------end----------