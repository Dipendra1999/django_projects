from django.template import loader 
from django.http import HttpResponse
from .models import Member
from django.shortcuts import render


# Create your views here.

def members(request):
    mymembers=Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    detail=Member.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mymembers':detail,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template=loader.get_template('template.html')
    fruits=['apple','banana','orange','dragonfruit' ]
    context={
        'fruits':fruits,
    }
    return HttpResponse(template.render(context,request))

def add(request):
#    template=loader.get_template('result.html')
    num1=int(request.POST.get('num1'))
    num2=int(request.POST.get('num2'))
#    context={
#        'result':num1+num2,
#    }
#    return HttpResponse(template.render(context,request))
    return render(request,'result.html',{'result':num1+num2})

def addition(request):
    template=loader.get_template('addition.html')
    return HttpResponse(template.render({'name':'Dipu'},request))