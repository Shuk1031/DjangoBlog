from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

urlpatterns= [
    path('create/', BlogCreateView.as_view(), name='blog/create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog/update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog/delete'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog/detail'),
]