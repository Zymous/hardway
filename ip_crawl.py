# -*- coding: utf-8 -*-
import requests
import pdb
import redis
import threading
import multiprocessing
import time

r = redis.Redis(host="127.0.0.1",port=6379,db=1)
# print r.lpop('tq')

def url_craw():
    while r.llen('tq2'):
        try:
            mac = r.brpop('tq2',0)[1]
            if r.exists(mac):
                continue
            url = 'http://222.73.156.130:8100/router-firmware-update/router/wanIp?mac=%s' % mac
            html = requests.get(url)
            r.set(mac,html.text)
        except:
            r.lpush('tq',mac)

#多线程处理
def thread_handle():
    threads=[]
    while threads or r.llen('tq2'):
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while r.llen('tq2'):
            thread = threading.Thread(target=url_craw)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
            time.sleep(5)
    exit(0)
def multi_process():
    processes = []
    #num_cpus = multiprocessing.cpu_count()
    #pool = multiprocessing.Pool(5)
    for i in range(2):
        p = multiprocessing.Process(target=thread_handle)
        p.start()
        processes.append(p)
        time.sleep(2)
    # while self.red.llen('tq1'):
    #     pool.apply_async(self.thread_handle)
    for p in processes:
        p.join()
    return
thread_handle()
