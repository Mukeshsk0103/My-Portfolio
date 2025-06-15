import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


ALLOWED_EXTENSIONS = ['.pdf', '.docx']
UPLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'CV')


def home(request):
    return render(request, 'portfolio/index.html')


def download_file(request, filename):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        raise Http404("File not found")