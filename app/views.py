from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insertschool(request):
    ESFO=Schoolform()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sp=SFDO.cleaned_data['Sprincipal']
            sl=SFDO.cleaned_data['Slocation']
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['re_enteremail']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl,email=e,re_enteremail=re)[0]
            SO.save()
            return HttpResponse('School is created')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insertschool.html',d)