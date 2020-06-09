from django.shortcuts import render
from django.http import HttpResponse
from .models import patient_info
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("Hello Django!!")

class patient_list_view(generic.TemplateView) :

    def get(self, request, *args, **kwargs) :
        m_template = 'main.html'
        patient_info = patient_info.objects.all()
        return render(request, m_template, {'patient_info':patient_info})




    # def patient_visit_date_view()
    #
    #     return