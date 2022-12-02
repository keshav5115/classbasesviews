"""procbv URL Configuration

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

from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcreate/',views.userview,name='fcreate'),
    path('cbcreate/',views.userclassview.as_view(),name='cbcreate'),
    path('fupdate/<pk>/',views.userupdate,name='fupdate'),
    path('cbupdate/<pk>/',views.userupdateview.as_view(),name='cbupdate'),
    path('cbread/',views.userreadview.as_view(),name='cbread'),
    path('cbdelete/<pk>/',views.userdeleteview.as_view(),name='cbdelete'),
    path('pcbcreate/',views.createuserview.as_view(),name='pcbcreate'),
    path('pcbupdate/<pk>/',views.updateuserview.as_view(),name='pcbupdate'),
    path('pcblist/',views.listuserview.as_view(),name='pcblist'),
    path('pcbdetail/<pk>/',views.detailuserview.as_view(),name='pcbdetail'),
    path('pcbdelete/<pk>/',views.deleteuserview.as_view(),name='pcbdelete'),
]
