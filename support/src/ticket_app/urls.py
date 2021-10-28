from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ticket_app import views

router = DefaultRouter()
router.register(r'ticket', views.TicketViewSet, basename='Ticket')

urlpatterns = [
    path('', include(router.urls)),
]
