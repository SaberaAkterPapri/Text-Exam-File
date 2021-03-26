from django.urls import path
from examtest import views

urlpatterns = [
    path('', views.search_list),
    path('keyword-list', views.keyword_list),
]