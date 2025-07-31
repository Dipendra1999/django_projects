from django.template import loader
from django.http import HttpResponse
from .models import Member
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
