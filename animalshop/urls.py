from django.urls import path
from animalshop import views

urlpatterns = [
    path('get_animals/', views.get_animals),
    path('get_animal/<int:pk>/', views.get_animal),
    path('create_animal/', views.create_animal),
    path('update_animal/<int:pk>/', views.update_animal_info),
    path('delete_animal/<int:pk>/', views.delete_animal),
    path('get_orders/', views.get_orders),
    path('get_order/<int:pk>/', views.get_order),
    path('create_order/', views.create_order),
    path('update_order/<int:pk>/', views.update_order_info),
    path('delete_order/<int:pk>/', views.delete_order),
]
