from django.contrib import admin
from django.http.response import JsonResponse
from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('', lambda request: JsonResponse({"status": "success", "message": "Home page"})),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('habits/', include('habits.urls', namespace='habits')),

    # Документация
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
