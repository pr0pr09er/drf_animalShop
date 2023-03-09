"""
URL configuration for animalshops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from animalshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get_animals/', views.get_animals),
    path('api/v1/get_animal/<int:pk>/', views.get_animal),
    path('api/v1/create_animal/', views.create_animal),
    path('api/v1/update_animal/<int:pk>/', views.update_animal_info),
    path('api/v1/delete_animal/<int:pk>/', views.delete_animal),
    path('api/v1/get_orders/', views.get_orders),
    path('api/v1/get_order/<int:pk>/', views.get_order),
    path('api/v1/create_order/', views.create_order),
    path('api/v1/update_order/<int:pk>/', views.update_order_info),
    path('api/v1/delete_order/<int:pk>/', views.delete_order),
]
