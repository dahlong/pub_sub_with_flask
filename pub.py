import redis

#queue = redis.StrictRedis(host='localhost', port=6379, db=0)
queue = redis.Redis('localhost')
channel = queue.pubsub()

#for i in range(10):
#    queue.publish("test", i)
#    time.sleep(0.5)

with open('./test.log') as f:
  while True:
    line = f.readline()
    if line:
      print line,' was sent to redis...'
      queue.publish("test", line)
