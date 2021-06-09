from django.conf.urls import url
from rest_framework.views import APIView
import requests
from django.http import JsonResponse, response
import urllib.request , json
from functools import lru_cache            
from rest_framework.response import Response

def ping(request):
    url=request.POST.get("url")
    response=requests.get(url)

    data=response.json()
    #urllib.request.urlopen(url,data=None)
    #res=urllib.request.Request(url1,data=None)
    #data = json.loads(url.read().decode())
    print("Check_____",data)
    return JsonResponse(url, safe=False)
    
    
    # print("Check1____________",url1,data)
    # message="Successfull"
    
    # return JsonResponse(data)
#try:

        # url="https://www.foobar.com"
        # response=urllib.request.Request(url,data=None)
        #     #data = json.loads(url.read().decode())
        # print("Data_____________",response)
        # return JsonResponse(response,safe=False)
    # except urllib.error.URLError as e:
    #     print(e.reason)
    
    #     return JsonResponse(response,safe=False)

def info(request):
    payload={
        "Receiver": "Cisco is the best!"
    }
    return JsonResponse(payload)