from django.contrib import admin
from django.urls import path, include


import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Thirds App URL
    path('notifications/', include(notifications.urls, namespace='notifications')),

    # API URL
    path('api/v1.0/', include('administration.urls')),

    
]
