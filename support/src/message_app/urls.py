from django.urls import include, path
from message_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'message', views.MessageViewSet, basename='Message')

urlpatterns = [
    path('', include(router.urls)),
]
