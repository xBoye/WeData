from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Teacher, Student, Course, Sc
import json

def index(request):
    '''主页'''
    #return HttpResponse('hello world!')
    return render(request,'student/index.html')
	
def scorelists(request):
    '''成绩删除'''
    print('request.get_full_path():',request.get_full_path())
    print('request.GET:',request.GET)
    print('request.user:',request.user)
    scs = Sc.objects.all()
    paginator = Paginator(scs, 10)  #每页10行
  
    page = request.GET.get('page')
    try:
        scs = paginator.page(page)
    except PageNotAnInteger:
        scs = paginator.page(1)
    except EmptyPage:
        scs = paginator.page(paginator.num_pages)
	
    context = {'scs':scs}
    return render(request, 'student/scorelists.html', context)

def delete_score_by_id(request):
    """按成绩编号删除"""
    print('request.get_full_path():',request.get_full_path())
    print('request.META["REMOTE_ADDR"]:',request.META["REMOTE_ADDR"])
    print('request.user:',request.user)
    print("request.GET['id']:", request.GET['id'])
    if not request.GET['id']:
        return render(request,'err404.html',{'msg':'id is null！'})
    id = int(request.GET.get('id'))
    if not Sc.objects.filter(id=id).exists():
        #return HttpResponseRedirect('http://localhost:8000/student/index/')
        return render(request,'err404.html',{'msg':'id Not Found！'})
    Sc.objects.get(id=id).delete()
    scs = Sc.objects.all()
	
    paginator = Paginator(scs, 10)  #每页10行
  
    page = request.GET.get('page')
    try:
        scs = paginator.page(page)
    except PageNotAnInteger:
        scs = paginator.page(1)
    except EmptyPage:
        scs = paginator.page(paginator.num_pages)
	
	
    context = {'scs': scs}
    return render(request,'student/scorelists.html',context)