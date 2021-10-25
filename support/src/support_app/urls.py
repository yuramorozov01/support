"""support URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('ticket/', views.TicketViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('ticket/<int:pk>/', views.TicketViewSet.as_view({
        'get': 'retrieve', 
        'delete': 'destroy', 
        'put': 'update', 
        'patch': 'partial_update'
    })),

    path('message/', views.MessageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('message/<int:pk>/', views.MessageViewSet.as_view({
        'get': 'retrieve', 
        'delete': 'destroy', 
        'put': 'update', 
        'patch': 'partial_update'
    })),
]
