import requests

import shutil
import os
# SOAP request URL

url = "http://172.16.110.52:3013/VENDASLOJA.apw"
  
# structured XML
payload = """<?xml version="1.0" encoding="utf-8"?"
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
                xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CFILIALLOGIN>13</CFILIALLOGIN> 
                </soap:Body>
            </soap:Envelope>"""
# headers
headers = {
    'Content-Type': 'text/html; charset=iso-8859-1'
}
# POST request
response = requests.request("POST", url, headers=headers, data=payload)

  
res = response.text

# prints the response
log = open("vouembora.log", "a")

#for arquivo in os.listdir(os.getcwd()):
#    if ".txt" in arquivo:
#        print(arquivo)

#if os.path.exists():
    
#print(os.getcwd())

#shutil.copy2(arquivo, os.getcwd())

log.write(res)

#print(response.text)
#print(response)