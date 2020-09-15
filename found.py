#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'http://fundf10.eastmoney.com/jjjz_000913.html'
url1 = 'http://fundf10.eastmoney.com/jjjz_001510.html'
url2 = 'http://fundf10.eastmoney.com/jjjz_200008.html'

# fp = open('content.txt','a')
#
# r = requests.get(url = url , verify = False)
#
# fp.write('%s\n'%str(r.content))
#
# jz = re.findall('<span id="fund_gszf" class="red lar bold ">(.*?)</span>',r.content)
# up_down = re.findall('<span id="fundgz_icon" class="icon  (.*?)"></span>',r.content)[0].split('-')
#
# print up_down
# print jz

def sendmail(send_text):
    # 第三方 SMTP 服务
    mail_host = ""
    mail_user = ""
    mail_pass = "KNZVOVIAFKCNIVYW"

    sender = ''
    receivers = ['','']
    text = '<h1>'+send_text+'</h1></p>'

    message = MIMEText(text, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receivers[0]

    subject = '基金报告来了（每五分钟）'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "sendsuccess"
    except smtplib.SMTPException as e:
        print e

def check():
    num = 0
    while True:
        try:
            flag = ''
            r_000913 = requests.get(url = url , verify = False)
            jz_000913 = re.findall('<span id="fund_gszf" class="red lar bold ">(.*?)</span>', r_000913.content)
            up_down_00913 = re.findall('<span id="fundgz_icon" class="icon  (.*?)"></span>', r_000913.content)[0].split('-')[1]
            shouyi_000913 = 20000*float(jz_000913[0].split('%')[0])/100
            if 'up' in up_down_00913:
                print '农银医疗保健股票 (000913)基金 - 上涨'
                print '农银医疗保健股票 (000913)净值 - %s'%str(jz_000913)
                num = num + 1
            else:
                print '农银医疗保健股票 (000913)基金 - 下跌'
                print '农银医疗保健股票 (000913)值 - %s' % str(jz_000913)
            print '农银医疗保健股票 (000913)基金收益 - '+str(shouyi_000913)+'元'
            r_001510 = requests.get(url = url1 , verify = False)
            jz_0001510 = re.findall('<span id="fund_gszf" class="red lar bold ">(.*?)</span>', r_001510.content)
            up_down_0001510 = re.findall('<span id="fundgz_icon" class="icon  (.*?)"></span>', r_001510.content)[0].split('-')[1]
            shouyi_0001510 = 20000*float(jz_0001510[0].split('%')[0])/100
            if 'up' in up_down_0001510:
                print '富国新动力灵活配置混合C (001510)基金 - 上涨'
                print '富国新动力灵活配置混合C (001510)净值 - %s'%str(jz_0001510)
                num = num + 1
            else:
                print '富国新动力灵活配置混合C (001510)基金 - 下跌'
                print '富国新动力灵活配置混合C (001510)值 - %s' % str(jz_0001510)
            print '富国新动力灵活配置混合C (001510)基金收益 - %s'%str(shouyi_0001510)+'元'
            r_200008 = requests.get(url=url2, verify=False)
            jz_200008 = re.findall('<span id="fund_gszf" class="red lar bold ">(.*?)</span>', r_200008.content)
            up_down_200008 = \
            re.findall('<span id="fundgz_icon" class="icon  (.*?)"></span>', r_200008.content)[0].split('-')[1]
            shouyi_200008 = 10000*float(jz_200008[0].split('%')[0])/100
            if 'up' in up_down_200008:
                print '长城品牌优选混合 (200008)基金 - 上涨'
                print '长城品牌优选混合 (200008)净值 - %s' % str(jz_200008)
                num = num + 1
            else:
                print '长城品牌优选混合 (200008)基金 - 下跌'
                print '长城品牌优选混合 (200008)净值 - %s' % str(jz_200008)
            print '长城品牌优选混合 (200008)基金收益 - %s'%str(shouyi_200008)+'元'
            res = '长城品牌优选混合 (200008)基金涨跌幅' + str(jz_200008) + \
                  ':收益 - '+str(shouyi_200008)+'元</p>\n 富国新动力灵活配置混合C (001510)基金涨跌幅'+ str(jz_0001510) + \
                  ':收益 - '+str(shouyi_0001510)+'元</p>\n 农银医疗保健股票 (000913)基金涨跌幅'+str(jz_000913)+':收益 - '+str(shouyi_000913)+'元</p>'
            print res
            sendmail(send_text=res)
        except Exception as e:
            print e
        time.sleep(20)
        print num
        # print res
        print '-'*55

check()
# print time.time()


