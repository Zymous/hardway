import redis
import os as a
import json

r = redis.Redis(host="192.168.2.135",port=6379,db=1)

for i in a.listdir(r'/var/bigdata/learnbydoing/sd/source_data'):
    file_path = '/var/bigdata/learnbydoing/sd/source_data/' + i
    date = i.split('_')[0]
    with open(file_path) as f:
        for line in f:
            key = line.split('\\')[0]
            r.hmset(key,{date:1})
