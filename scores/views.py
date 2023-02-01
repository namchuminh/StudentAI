from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from students.models import ClassName, Specialization
from subjects.models import Subject
from user.models import InfoUser
from django.http import JsonResponse
from .models import Scores

# Create your views here.

class Index(View):
    template_name =  'scores/index.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Index, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        subjects = Subject.objects.all().filter(infouser=infouser)
        
        specialization_list = Specialization.objects.all()
        
        
        data = {
            'title': 'Quản Lý Điểm Môn Học - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'subjects': subjects,
            'specialization_list': specialization_list,
            
        }
        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        
        if request.POST['specializationpk'] is not None:
            specializationpk = request.POST['specializationpk']
            specialization = Specialization.objects.all().get(pk=specializationpk)
            subjects = Subject.objects.all().filter(specialization=specialization).values('pk','name','credits','teaching','specialization__name','slug',)

            data = list(subjects)

            return JsonResponse({'data': data})
        
    
class ClassSubject(View):
    
    template_name =  'scores/classsubject.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(ClassSubject, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, slug, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        try: 
            subject = Subject.objects.all().get(slug=slug)
            specialization = subject.specialization
            classname = ClassName.objects.all().filter(specialization=specialization)
            
            data = {
                'title': 'Quản Lý Điểm Môn Học - StudentAI',
                'fullname': infouser.user.first_name + " " + infouser.user.last_name,
                'avatar': infouser.avatar,
                'specialization': infouser.specialization,
                'classname': classname,
                'subject_name': subject.name,
                'subject_slug': subject.slug
            }
            return render(request,self.template_name,data)
        except:
            return redirect('index_scores')

class ScoresSubject(View):
    
    template_name =  'scores/scores.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(ScoresSubject, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, slug_subject, slug_class, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        try:
            
            subject = Subject.objects.all().get(slug=slug_subject)
            classname = ClassName.objects.all().get(slug=slug_class)
            
            scores = Scores.objects.all().filter(subject=subject, classname=classname).order_by('pk')
            
            data = {
                'title': 'Quản Lý Điểm Môn Học - StudentAI',
                'fullname': infouser.user.first_name + " " + infouser.user.last_name,
                'avatar': infouser.avatar,
                'specialization': infouser.specialization,
                'scores': scores,
                'subject_name': subject.name,
                'classname': classname.name,
            }
            return render(request,self.template_name,data)
        except:
            return redirect('index_scores')
        