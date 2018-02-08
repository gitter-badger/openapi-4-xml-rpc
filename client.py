#!/usr/bin/env python3

from  xmlrpc.client import ServerProxy, ProtocolError, ResponseError, Fault

host = "localhost"
port = "8080"
urlEndPoint="http://"+host+":"+port+"/users"

proxy = ServerProxy(urlEndPoint,verbose=True)

testUser = "alec" # valid test data

try:
    result = proxy.userExists(testUser)
    print("\nCalled userExist() on user {},\nresult {}".format(
        testUser, result))

    result = proxy.getUserAllDetails(testUser)
    print("""Called getUserAllDetails() on user {},
UUID is {},
active status is {}""".format(
        testUser, result["UUID"], result["activeStatus"]))

except Fault as error:
    print("""\nCall to user API failed with xml-rpc fault!
reason {}""".format(
        error.faultString))

except ResponseError as error:
    print("""\nCall to user API failed with xml-rpc response error !
reason {}""".format(
        error.faultString))

except ProtocolError as error:
    print("""\nA protocol error occurred
URL: {}
HTTP/HTTPS headers: {}
Error code: {}
Error message: {}""".format(
        error.url, error.headers, error.errcode, error.errmsg))

except ConnectionError as error:
    print("\nConnection error. Is the server running? {}".format(error))


