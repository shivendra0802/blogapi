from django.urls import path
from rest_framework import views
from blog import views
from blog.views import PostList, PostDetail

urlpatterns = [
    # path('api/', views.PostAPI.as_view()),
    # path('api/<int:pk>/', views.PostAPI.as_view()),
    path('api/', views.PostList.as_view()),
    path('api/<int:pk>/', views.PostDetail.as_view()),
    #path('api/<int:pk>/', views.PostGeneUpdate.as_view()),
    #path('api'<int:pk>/', views.PostGeneRetrive.as_view()),
]