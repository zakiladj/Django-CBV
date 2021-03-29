from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.PostList.as_view(),name="post_list"),
    path('create/',views.PostCreat.as_view(),name="create_post"),
    path('<int:pk>',views.PostDetail.as_view(),name="post_detail"),
]
app_name = 'post'