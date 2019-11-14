import os
import socket


HostDir = {}

def DNSlist(): #将文件数据放入字典中
    file = input('File Path:')
    DnsList = open (file)
    for rel in DnsList:
        Host = rel[0]
        Type = rel[1]
        IP = rel[2]
        HostDir.setdefault('Host',[]).append(Host)
        HostDir.setdefault('Type',[]).append(Type)
        HostDir.setdefault('IP',[]).append(IP)

def get_ip():#h获取IP地址并执行ping
    os.system('service named reload')
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    # print(ip)
    ping = os.system('ping -c 2 ' + ip)
    if ping == 0:
        print('True')
    else:
        os.system("echo -e %s'\t'%s'\t' %s " %(HostDir['Host'][count],HostDir['Type'][count],HostDir['IP'][count] + ">> False.log" ))

def Test(): #开始增加
    count = 0
    file = r'C:\Users\17763\Desktop\dns.txt'
    LocalFile = open(file)
    for RelH in HostDir['Host']:
        # print(RelH)
        pass
    for Need in LocalFile:
        need = Need.strip('\n').split('\t')
        OdHost = need[0]
        OdIP = need[2]
        RelIP = HostDir['IP'][count]
        RelTy = HostDir['Type'][count]
        if RelH == OdHost: #如果域名存在则更换IP,不在则新增
            # print('yes')
            os.system("sed 's/" + OdIP + "/" + RelIP + "/" + " " + file)
            get_ip()
        else:
            os.system("echo -e %s'\t'%s'\t'%s" %(RelH,RelTy,RelIP) + " >> " + file)
            get_ip()
    else:
        count +=1
        global count
try:
    DNSlist()
    Test()
except IndexError:
    pass
