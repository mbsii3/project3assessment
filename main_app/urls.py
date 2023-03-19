from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.items_index, name='items_index'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
]