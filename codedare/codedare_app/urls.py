from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.PostsListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostsDetailView.as_view(), name='detail'),
    path('posts/new/', views.PostsCreateView.as_view(), name='new'),
    path('posts/<int:pk>/edit', views.PostsUpdateView.as_view(), name='edit'),
    path('posts/<int:pk>/delete', views.PostsDeleteView.as_view(), name='delete'),
    path('posts/<int:pk>/comment', views.CommentCreateView.as_view(), name='comment'),
    path('posts/categories', views.categories_view, name='categories'),
    path('posts/categories/<str:pk>', views.categories_detail_view, name='categories'),
    
    
]