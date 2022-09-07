from lib2to3.pgen2.grammar import opmap
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from home import views

from django.urls import path, include

admin.site.site_header = "Login to Developer Shami"             # Admin Custom work 
admin.site.site_title = "Welcome to Shami's Dashboard"          # Admin Custom work
admin.site.index_title = "Welcome to this Portal"               # Admin Custom work

urlpatterns = [
    path('',views.home, name='home'),
    path('projects',views.projects, name='projects'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact')

]
