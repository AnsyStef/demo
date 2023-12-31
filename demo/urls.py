from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("main.urls")),
    path('admin/', admin.site.urls),
]
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 