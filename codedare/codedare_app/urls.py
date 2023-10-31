from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.detail_post, name='detail')
]