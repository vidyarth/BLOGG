from django.urls import path
from .views import userregistration
urlpatterns = [
    path('register/', userregistration.as_view(), name = "register")
]
