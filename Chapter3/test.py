import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
r.set('foo', 'bar')
r.set('foo', """{
    1,2,3,4,5,6
}""")
print(r.get('foo'))
