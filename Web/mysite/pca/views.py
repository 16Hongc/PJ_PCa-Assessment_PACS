from django.shortcuts import render
from django.http import HttpResponse
from .models import patient_info

# Create your views here.

# def index(request):
#     return HttpResponse("Hello Django!!")

def main(request):
    patient_list = patient_info.objects.all()
    return render(request, 'pca/dist/index.html', {'patient_list':patient_list})

# def patient_list(request) :
#     patient_db = patient_info.objects.all()
#     return render(request, 'pca/main.html')