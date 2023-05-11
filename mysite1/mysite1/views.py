# my creation
"""we have to give an http response becz the views retuens an http response"""

from django.http import HttpResponse
html_string=""
with open('mysite1/execise1.html', 'r') as f:
    html_string+=(f.read())

def index(request): # ye index takes an argument by default which is request
    return HttpResponse(html_string) # using an html here

def about(request): # koi bhi function not only the index takes an argument by default which is request
    return HttpResponse("about hello")