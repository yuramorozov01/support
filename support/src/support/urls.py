from django.contrib import admin
from django.urls import include, path

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('api/v1/', include('ticket_app.urls')),
    path('api/v1/', include('message_app.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls
