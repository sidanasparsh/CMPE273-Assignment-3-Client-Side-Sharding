import httplib
import json
#from HRW
from consistentHashing import ConsistentHashRing

cr1=ConsistentHashRing()
print (cr1.hashObject('1'))

nodes = {"127.0.0.1:3000", "127.0.0.1:4000", "127.0.0.1:5000"}
for url in nodes:
    hashedUrl=cr1.hashObject(str(url))
    cr1.__setitem__(hashedUrl, url)
i=1
for i in range(1,11):
    print i
    destinationNode=cr1.__getitem__(str(i))
    headers = {'Content-type': 'application/json'}
    conn = httplib.HTTPConnection(destinationNode)
    print "Response from: ",destinationNode
    foo = { "id" : str(i),
    "name" : "Foo 2",
    "email" : "foo2@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "800",
    "submit_date" : "12-10-2016"}
    json_foo = json.dumps(foo)
    conn.request('POST', 'v1/expenses', json_foo, headers)
    response = conn.getresponse()
    print(response.read().decode())

for i in range(1,11):
    destinationNode = cr1.__getitem__(str(i))
    headers = {'Content-type': 'application/json'}
    conn = httplib.HTTPConnection(destinationNode)
    print "Response from: ", destinationNode
    foo = {"id": str(i),
           "name": "Foo 2",
           "email": "foo2@bar.com",
           "category": "office supplies",
           "description": "iPad for office use",
           "link": "http://www.apple.com/shop/buy-ipad/ipad-pro",
           "estimated_costs": "800",
           "submit_date": "12-10-2016"}
    json_foo = json.dumps(foo)
    conn.request('GET', 'v1/expenses/'+str(i), json_foo, headers)
    response = conn.getresponse()
    print(response.read().decode())