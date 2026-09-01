from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.http.response import JsonResponse

urlpatterns = [
    path('', lambda request: JsonResponse({"status": "success", "message": "Home page"})),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
]
