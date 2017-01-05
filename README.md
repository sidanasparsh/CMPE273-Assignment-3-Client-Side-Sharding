# CMPE273-Assignment-3-Client-Side-Sharding

Implemented client-side sharding for the expense management application that you built in the assignment 1.

##Features

1. Modify existing POST /v1/expenses endpoint so that it can take "id" as input instead of server generated id.

2. Three (Docker - optional) the expense management applicaiton instances - each application instance uses its own MySQL instance.

3. Three (Docker - optional) MySQL DB instances mounted to three different local paths so that each one will have different data set.

## Consistent Hashing

* Use id as the shard key.
* Correct consistent hashing client should shard the following ten expenses into multiple back-end instances.

* Consistent hashing client implementation is in a file called ch_client.py with the following steps:

* 1. Defined three expense management applications hostnames in an array or set. E.g. nodes = {"127.0.0.1:3000", "127.0.0.1:4000", "127.0.0.1:5000"}

* 2. Implemented a consistent hashing function that can take "id" as key, do all consistent hashing logic, and finally returned one
of the nodes from the above list.

* 3. Looped through 10 ids (0-9) and get the node mapping: "1" => "127.0.0.1:3000", "2" => "127.0.0.1:4000", etc.

* 4. Made a HTTP POST call to http://{node_returned_from_consistent_hashing_function}/v1/expenses for each id.

##Test Data and Responses:

*Request 1

```
{
    "id" : "1",
    "name" : "Foo 1",
    "email" : "foo1@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "12-10-2016"
}
```

*Request 2

```
{
    "id" : "2",
    "name" : "Foo 1",
    "email" : "foo1@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "12-10-2016"
}
```
...

*Request 10

```
{
    "id" : "10",
    "name" : "Foo 1",
    "email" : "foo1@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "12-10-2016"
}
```

**Response:**
###GET Responses from all the servers (Request id from 1-10):
```
Response from: 127.0.0.1:3000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 1, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:3000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 2, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:3000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 3, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:3000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 4, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:3000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 5, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:5000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 6, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:4000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 7, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:3000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 8, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:5000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 9, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}

Response from: 127.0.0.1:3000 {"category": "office supplies", "decision_date": "", "description": "iPad for office use",
"email": "foo2@bar.com", "estimated_costs": "800", "id": 10, "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name":
"Foo 2", "status": "Pending", "submit_date": "12-10-2016"}
```

