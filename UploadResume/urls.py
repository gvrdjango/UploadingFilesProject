from django.urls import path
from .views import *

urlpatterns = [

    path('', UploadProfile, name='index'),
    path('viewprofiles/', ViewProfiles, name='viewprofiles'),

    path('jobs/', Jobs, name='jobs'),
    path('contact/', Contact, name='contact'),
]
