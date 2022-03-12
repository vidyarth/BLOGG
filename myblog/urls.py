from django.urls import path, include
from .views import homeview, articleview,addpost,updatepost,deletepost
urlpatterns = [
    path('', homeview.as_view(), name = "home"),
    path('article/<int:pk>', articleview.as_view(), name = "article"),
    path('add',addpost.as_view(), name="add"),
    path('article/update/<int:pk>', updatepost.as_view(), name="update"),
    path('article/delete/<int:pk>', deletepost.as_view(), name="delete"),
]
