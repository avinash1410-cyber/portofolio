from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import jobs

# Create your views here.
def home(request):
    Jobs=jobs.objects.all()
    return render(request,'jobs/home.html',{'Jobs':Jobs})

def detail(request,id):
    J_detail=get_object_or_404(jobs,pk=id)
    return render(request,'jobs/detail.html',{'Job_detail':J_detail})