#!/usr/bin/python
# coding = utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import asyncio

SMTP_SERVER = 'smtp.qq.com'
POPS_SERVER = 'pop.qq.com'
FROM_ADDR = '519616828@qq.com'
PASSWORD = 'ixefccfhuwrkcahc'
TO_ADDR = 'chenshaoting@justguard.cn'
MESSAGE = '我遇到麻烦了。 from MacBookAir。authCode:ixefccfhuwrkcahc'

def send(message):
    server = smtplib.SMTP()
    server.connect(SMTP_SERVER,25)
    server.login(FROM_ADDR,PASSWORD)

    try:

        server.sendmail(FROM_ADDR,TO_ADDR,message)

        print('mail sent successfully.')
        return True
    except:
        print('failed to send mail.')
        return False


def makeMessage(msg = MESSAGE):
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header(FROM_ADDR, 'utf-8')   # 发送者
    message['To'] = Header(TO_ADDR, 'utf-8')        # 接收者

    subject = 'Stock Price Changed'
    message['Subject'] = Header(subject, 'utf-8')
    return message

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset



def print_info(msg):
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            if header == 'Subject':
                value = decode_str(value)
            else:
                hdr, addr = parseaddr(value)
                name = decode_str(addr)
                value = name + ' < ' + addr + ' > '
        print(header + ':' + value)
    for part in msg.walk():
        filename = part.get_filename()
        content_type = part.get_content_type()
        charset = guess_charset(part)
        if filename:
            filename = decode_str(filename)
            data = part.get_payload(decode = True)
            if filename != None or filename != '':
                print('Accessory,found but not saved: ' + filename)
                # savefile(filename, data, mypath)
        else:
            email_content_type = ''
            content = ''
            if content_type == 'text/plain':
                email_content_type = 'text'
            elif content_type == 'text/html':
                email_content_type = 'html'
            if charset:
                content = part.get_payload(decode=True).decode(charset)
            print(email_content_type + ' ' + content)

async def fetchPopMail():
    server = poplib.POP3(POPS_SERVER, 110)
    #print(server.getwelcome())
    server.user(FROM_ADDR)
    server.pass_(PASSWORD)
    print('Message: %s. Size: %s' % server.stat())

    resp, mails, objects = server.list()
    #print(mails)
    index = len(mails)
    #取出某一个邮件的全部信息
    resp, lines, octets = server.retr(index)
    #邮件取出的信息是bytes，转换成Parser支持的str
    lists = []
    for e in lines:
        lists.append(e.decode())
    msg_content = '\r\n'.join(lists)
    # print(msg_content)
    msg = Parser().parsestr(msg_content)
    # print(msg)
    print_info(msg)
    # server.dele(index)
    #提交操作信息并退出
    server.quit()

if __name__ == '__main__':
    list=[
        "002279",
        "002432",
        "002466",
        "002594",
        "600026",
        "601012",#above remen, below longtou
        "000988",
        "002030",
        "002311",
        "002432",
        "002460",
        "002466",
        "002556",
        "002594",
        "002758",
        "600256",
        "600481",
        "600499",
        "600941",
        "601225",
        "601238",
        "601965",
        "603100",
        "603868",]
    message = '\npotential:%s' % (list)
    send(makeMessage(message).as_string())
    # loop = asyncio.new_event_loop()


