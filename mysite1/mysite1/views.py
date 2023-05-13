# my creation
"""we have to give an http response becz the views retuens an http response"""

from django.http import HttpResponse
from django.shortcuts import render

"""html_string=""
with open('mysite1/execise1.html', 'r') as f:
    html_string+=(f.read())

#print(html_string)
def index(request): # ye index takes an argument by default which is request
    return HttpResponse(html_string) # using an html here

def about(request): # koi bhi function not only the index takes an argument by default which is request
    return HttpResponse("about hello")
"""# this is the exercise1 code


"""Back button is made by <a herf='/'>back</a> this a tag"""

#adding an back button
html_string=""
with open('mysite1/backbutton.html', 'r') as f:
    html_string+=(f.read())

def index(request):
    return render(request,'index.html')
# this uses the html file named index in the index folder which is being displayed in the web this is the easier way to manage the pages

def rm_punctua(request):
    return HttpResponse(html_string)

def capital(response):
    return HttpResponse(html_string)

def newline_remove_first(response):
    return HttpResponse(html_string)

def space_remover(response):
    return HttpResponse(html_string)

def charcount(response):
    return HttpResponse(html_string)