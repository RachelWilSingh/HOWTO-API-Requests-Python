import requests
import json

# Simple example of using Python to make API calls, useful for testing microservices...
# Using these calls to test with: https://docs.postman-echo.com/?version=latest
# Requests homepage: https://2.python-requests.org/en/master/

header = {"Content-Type": "application/json"}
token = None

def PrintJson( jsontext ):
    parsed = json.loads( jsontext )
    print( json.dumps( parsed, indent=4, sort_keys=True ) )


def Authenticate( header ):
    url = ""
    body = {
    }
    bodyJson = json.dumps( body )
    
    response = response.post( url, data=bodyJson, headers=header )
    print( response.status_code )
    PrintJson( response.content )
        
    token = response.json()["access_token"]
    
    return token

# token = Authenticate( header )


# - POST requests ---------------------------------------------------- #
def PostRequest( header ):
    print( "\n\n Post request..." )
    
    url = "https://postman-echo.com/post"
    body = {
        "item1" : "value1"
    }
    bodyJson = json.dumps( body )
    
    response = requests.post( url, data=bodyJson, headers=header )
    print( response.status_code )
    PrintJson( response.content )
    
PostRequest( header )

# - GET requests ----------------------------------------------------- #
def GetRequest( header ):
    print( "\n\n Get request..." )
    
    url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
    
    response = requests.get( url, headers=header )
    print( response.status_code )
    PrintJson( response.content )

GetRequest( header )

# - PUT requests ----------------------------------------------------- #
def PutRequest( header ):
    print( "\n\n Put request..." )
    
    url = "https://postman-echo.com/put"
    body = {
        "item1" : "value1"
    }
    bodyJson = json.dumps( body )
    
    response = requests.put( url, data=bodyJson, headers=header )
    print( response.status_code )
    PrintJson( response.content )

PutRequest( header )

# - PATCH requests --------------------------------------------------- #
def PatchRequest( header ):
    print( "\n\n Patch request..." )
    
    url = "https://postman-echo.com/patch"
    body = {
        "item1" : "value1"
    }
    bodyJson = json.dumps( body )
    
    response = requests.patch( url, data=bodyJson, headers=header )
    print( response.status_code )
    PrintJson( response.content )

PatchRequest( header )


