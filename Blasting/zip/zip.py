#!/usr/bin/python

import zipfile
import threading

def zipbp(zfile,pwd):
    try:
        zfile.extractall(pwd=pwd)
        print 'password found : %s' % pwd
    except:
        return

def main():
    zfile = zipfile.ZipFile('test.zip')
    pwdall = open('dict.txt')
    for pwd in pwdall.readlines():
        pwd = pwd.strip('\n')
        t = threading.Thread(target=zipbp,args=(zfile,pwd))
        t.start()

if __name__ == '__main__':
    main()

'''
password found : 123456
'''
