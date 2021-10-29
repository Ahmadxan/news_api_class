from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/detail/', views.CategoryDetail.as_view()),

    path('news/', views.NewsList.as_view()),
    path('news/<int:pk>/detail/', views.NewsDetail.as_view()),

    path('commits/', views.CommitList.as_view()),
    path('commits/<int:pk>/detail/', views.CommitDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/detail/', views.UserDetail.as_view()),
]
