from django.contrib import admin
from django.urls import path, re_path, include
from tesseract_ocr import views as ans


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', ans.index, name='index'),
    re_path(r'^tesseract_ocr/', include('tesseract_ocr.urls'), name='tesseract_ocr'),
]
