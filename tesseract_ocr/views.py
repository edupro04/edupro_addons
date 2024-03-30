from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(request):
    print('hello')
    print(request.FILES.get('pro-image'))
    if request.method == 'POST' and request.FILES.get('pro-image'):
        uploaded_image = request.FILES['pro-image']

        # Save the uploaded image to a temporary location
        temp_image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image.png')
        with open(temp_image_path, 'wb') as temp_image_file:
            for chunk in uploaded_image.chunks():
                temp_image_file.write(chunk)

        # Open the saved image using PIL (Python Imaging Library)
        image = Image.open(temp_image_path)

        # Perform OCR on the image using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        # Delete the temporary image file
        os.remove(temp_image_path)

        return JsonResponse({'extracted_text': extracted_text})

    return JsonResponse({'error': 'No image uploaded or invalid request method'})
