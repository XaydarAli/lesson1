from django.urls import path
from .views import home,account,groups,login,register
urlpatterns=[
    path('',home,name='home'),
    path('account/',account,name='account'),
    path('groups/',groups,name='groups'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]
