from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('extract_text_from_image/', views.extract_text_from_image, name='extract_text_from_image'),
]
