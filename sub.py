import redis
import time

#r = redis.StrictRedis(host='localhost', port=6379, db=0)
r = redis.Redis('localhost')
p = r.pubsub()
p.subscribe('test')

while True:
    message = p.get_message()
    if message:
	print message       
	print "Subscriber: %s" % message['data']
    time.sleep(1)
