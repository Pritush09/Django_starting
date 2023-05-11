# mappings define hoti he
"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #first argument is he url ke baad kya end point he ,  function which need to be run when someone visit your that endpoint,
    # uska naam taki bada sa endpoint ho toh usse bulla sake
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),#kuch nahi str me toh home page hota he
    path("about",views.about, name="about")
]
