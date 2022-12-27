from django.urls import path

from . import views

app_name = 'blogi'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:post_id>/read/', views.read, name='read'),
]