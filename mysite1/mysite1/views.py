# my creation
"""we have to give an http response becz the views retuens an http response"""

from django.http import HttpResponse
def index(request): # ye index takes an argument by default which is request
    return HttpResponse("<h1>HELLO</h1>") # using an html here

def about(request): # koi bhi function not only the index takes an argument by default which is request
    return HttpResponse("about hello")