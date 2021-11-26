from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('auth/', include('authorization.urls')),
    path('finance/', include('finance.urls')),
]
