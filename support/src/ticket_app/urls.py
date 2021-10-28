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
]
