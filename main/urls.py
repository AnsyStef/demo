from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home),
    path('en/', views.home_eng)
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 