# funcaas
## Functions As A Service(1), the next obvious thing.

Staring at your belly button and wondering who really needs containers? Starting to think microservices have grown too large? Wish every function you needed for your next killer app was available with 92% uptime(2) just a simple jQuery.get() away?

1. Proper pronunciation is Funk-Ass.
2. Uptime not guaranteed.

### Methods Documentation

#### GET: /is/int/n
This method returns `{"result": True}` if _n_ is integer-ish, and `{"result": False}` otherwise.

#### POST: /format
Post a JSON payload like `{"string": "this is a list of {}, {}, and {}", "formatter", ["a", "b", "c"]}` using Python 3-style .format() semantics and you'll receive a response like `{"result": "this is a list of a, b, and c"}`, or an HTTP 500 on error.

#### GET or POST: /is/alive
Returns `{"result": "yes"}` if service is alive, otherwise returns `{"result": "no"}`

#### /return/true
Returns `{"result": True}`