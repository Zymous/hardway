import redis

r = redis.Redis(host="127.0.0.1",port=6379,db=1)

with open('D:\Python\hardway\mac.txt') as f:
    for line in f:
        mac = line.strip('\n')
        r.lpush('tq3',mac)
    exit(0)
