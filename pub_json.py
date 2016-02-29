import redis
import json

#queue = redis.StrictRedis(host='localhost', port=6379, db=0)
queue = redis.Redis('localhost')
channel = queue.pubsub()

#for i in range(10):
#    queue.publish("test", i)
#    time.sleep(0.5)

returnDict = {}

with open('./test_json.log') as f:
  while True:
    line = f.readline()
    words = line.split()
    for word in words:
        returnDict[word] = returnDict.get(word, 0) + 1


    json_objects = []
    for key, value in returnDict.iteritems():
        json_objects.append( {"word": key , "amount":value} )

    if line:
      print line,' got it...',json_objects,' was sent to redis'
      queue.publish("test", json.dumps(json_objects) )
