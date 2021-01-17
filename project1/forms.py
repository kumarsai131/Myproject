from PIL import Image
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
class ImageUploadForm(forms.Form):
    image=forms.ImageField()
