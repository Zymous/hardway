# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host="127.0.0.1",port=6379,db=1)

def write_result():
    while r.llen('tq3'):
        mac = r.brpop('tq3',0)[1]
        try:
            result = r.get(mac)
            ip = eval(result)['wanIp']
            if is_inner_ip(ip):
                with open('inner_ip.txt','a') as f:
                    f.write(mac + "\t" + ip + "\n")
            else:
                with open('outer_ip.txt','a') as f:
                    f.write(mac + "\t" + ip + "\n")
        except:
            with open('no_ip.txt','a') as f:
                f.write(mac + "\n")
def is_inner_ip(ip_addr):
    is_inner = False
    ipNum = get_ip_num(ip_addr)
    aBegin = get_ip_num("10.0.0.0")
    aEnd = get_ip_num("10.255.255.255")
    bBegin = get_ip_num("172.16.0.0")
    bEnd = get_ip_num("172.31.255.255")
    cBegin = get_ip_num("192.168.0.0")
    cEnd = get_ip_num("192.168.255.255")
    dBegin = get_ip_num("127.0.0.0")
    dEnd = get_ip_num("127.255.255.255")
    con1 = isInner(ipNum, aBegin, aEnd)
    con2 = isInner(ipNum, bBegin, bEnd)
    con3 = isInner(ipNum, cBegin, cEnd)
    con4 = isInner(ipNum, dBegin, dEnd)
    isInnerIp = con1 or con2 or con3 or con4
    return isInnerIp

def get_ip_num(ip_addr):
    ip = ip_addr.split('.')
    ip_num = int(ip[0]) * 256 * 256 * 256 + int(ip[1]) * 256 * 256 + int(ip[2]) * 256 + int(ip[3])
    return ip_num

def isInner(ip, begin, end):
    return (ip >= begin) and (ip <= end)

write_result()
