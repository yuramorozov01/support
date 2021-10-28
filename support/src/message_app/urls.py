from django.urls import path, include
from rest_framework.routers import DefaultRouter
from message_app import views

router = DefaultRouter()
router.register(r'message', views.MessageViewSet, basename='Message')

urlpatterns = [
    path('', include(router.urls)),
]
