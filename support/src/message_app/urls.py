from django.urls import path
from message_app import views

urlpatterns = [
    path('message/', views.MessageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('message/<int:pk>/', views.MessageViewSet.as_view({
        'get': 'retrieve', 
        'delete': 'destroy', 
        'put': 'update', 
        'patch': 'partial_update'
    })),
]
