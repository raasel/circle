import requests
import json



name = input("Enter Nickname ")

url = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfobyNickname'
myobj = {'nickname':name}

#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = {"x-api-key": "ca7bf505399cd270b9ba0da59a052523","x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})

#convert response to json format

    #parse the json to get the service ticket
response= x.text

#the 'demopage.asp' prints all HTTP Headers
#01044439830

json_object = json.loads(response)

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)