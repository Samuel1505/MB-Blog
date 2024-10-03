from django.contrib import admin
from django.urls import path
from blog.views import homepageview, aboutpageview, contactpageview, categorypageview, search_resultpageview, single_postpageview, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("",homepageview.as_view(),name="home"),
    path("about",aboutpageview.as_view(),name="about"),
    path("contact",contactpageview.as_view(),name="contact"),
    path("category",categorypageview.as_view(),name="category"),
    path("search_result",search_resultpageview.as_view(),name="search_result"),
    path("single-post",single_postpageview.as_view(),name="single_post"),
    path('details/<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('create', BlogCreateView.as_view(), name="create"),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>/', BlogDeleteView.as_view(),name="delete")
]