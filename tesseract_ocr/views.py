from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import os
import base64
import io
from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

def index(request):
    return render(request, 'index.html')
    
    
def image_to_text(request):
    return render(request, 'image_to_text.html',)
    

@csrf_exempt     
def extract_text_from_image(request):
    print('hello')
    print(request.POST.get('merged-image', ''))
    if request.method == 'POST' and request.POST.get('merged-image', ''):
        print('inside if')
        image_data = request.POST.get('merged-image').split(',')[1]  # Get base64 string after comma
        img_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(img_bytes))
        extracted_text = pytesseract.image_to_string(image)

        return JsonResponse({'extracted_text': extracted_text})

    return JsonResponse({'error': 'No image uploaded or invalid request method'})
