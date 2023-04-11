from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from students.models import ClassName, Specialization, Students
from subjects.models import Subject
from user.models import InfoUser
from django.http import JsonResponse
from .models import Scores

# Create your views here.


class Index(View):
    template_name =  'scores/index.html'
    student_template_name = 'scores/studentscores.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Index, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if request.session['isStudent'] == True:
            user = User.objects.all().get(pk=request.user.pk)
            s = Students.objects.all().get(user=user)
            subjects = Subject.objects.all().filter(specialization = s.specialization)
            scores = Scores.objects.all().filter(student = s)
            data = {
                'title': 'Trang Thông Tin Sinh Viên - StudentAI',
                'fullname': user.first_name + " " + user.last_name,
                'avatar': s.avatar,
                'specialization': s.specialization,
                'classname': s.classname.name,
                'subjects': subjects,
                'scores': scores
            }
            return render(request,self.student_template_name,data)
        
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
                'slug_class': classname.slug,
                'slug_subject': subject.slug,
            }
            return render(request,self.template_name,data)
        except:
            return redirect('index_scores')
        
    def post(self, request, *args, **kwargs):
        if request.POST['pk'] is not None:
            try:
                scores = Scores.objects.all().get(pk=request.POST['pk'])
                scores.score1 = float(request.POST['score1'])
                scores.score2 = float(request.POST['score2'])
                scores.score3 = float(request.POST['score3'])
                scores.save()
                return JsonResponse({'data': True})
            except:
                return JsonResponse({'data': False})

class AddScoresSubject(View):
    template_name =  'scores/addscoressubject.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(AddScoresSubject, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, slug_subject, slug_class, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        try:
            
            subject = Subject.objects.all().get(slug=slug_subject)
            classname = ClassName.objects.all().get(slug=slug_class)
            
            students = Students.objects.all().filter(classname=classname).order_by('fullname')
            
            data = {
                'title': 'Quản Lý Điểm Môn Học - StudentAI',
                'fullname': infouser.user.first_name + " " + infouser.user.last_name,
                'avatar': infouser.avatar,
                'specialization': infouser.specialization,
                'subject_name': subject.name,
                'classname': classname.name,
                'slug_class': classname.slug,
                'slug_subject': subject.slug,
                'students': students
            }
            return render(request,self.template_name,data)
        except:
            return redirect('index_scores')
    
    def post(self, request, slug_subject, slug_class, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
     
        subject = Subject.objects.all().get(slug=slug_subject)
        classname = ClassName.objects.all().get(slug=slug_class)
        
        students = Students.objects.all().filter(classname=classname).order_by('fullname')
        
        scores = Scores.objects.all().filter(subject=subject, classname=classname).order_by('pk')

        data = {
            'title': 'Quản Lý Điểm Môn Học - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'subject_name': subject.name,
            'classname': classname.name,
            'slug_class': classname.slug,
            'slug_subject': subject.slug,
            'students': students
        }
        
        try:
            
            s = Students.objects.all().get(pk=request.POST['student_pk'])
            check_s = Scores.objects.all().filter(student=s,subject = subject).count()
            
            if (request.POST['s1'] == "" or request.POST['s2'] == "" or request.POST['s3'] == ""):
                data['error'] = "Vui lòng không bỏ trống điểm!"
                return render(request,self.template_name,data)
            
            elif(float(request.POST['s1']) > 10 or float(request.POST['s2']) > 10 or float(request.POST['s3']) > 10):
                data['error'] = "Điểm chỉ trong khoảng từ 0 điểm - 10 điểm"
                return render(request,self.template_name,data)
            
            elif(float(request.POST['s1']) < 0 or float(request.POST['s2']) < 0 or float(request.POST['s3']) < 0):
                data['error'] = "Điểm chỉ trong khoảng từ 0 điểm - 10 điểm"
                return render(request,self.template_name,data)
            
            if check_s == 0:
                try:
                    s1 = float(request.POST['s1'])
                    s2 = float(request.POST['s2'])
                    s3 = float(request.POST['s3'])
                    scores = Scores(score1=s1, score2=s2,score3=s3,student=s,subject=subject)
                    scores.save()
                    data['success'] = "Thêm điểm môn học " + subject.name + ", cho sinh viên " + s.fullname + " thành công!"
                    return render(request,self.template_name,data)
                except:
                    data['error'] = "Điểm không hợp lệ, vui lòng nhập lại!"
                    return render(request,self.template_name,data)
            elif check_s != 0:
                try:
                    scores = Scores.objects.all().get(student=s)
                    scores.score1 = float(request.POST['s1'])
                    scores.score2 = float(request.POST['s2'])
                    scores.score3 = float(request.POST['s3'])
                    scores.save()
                    data['success'] = "Cập nhật điểm môn học " + subject.name + ", cho sinh viên " + s.fullname + " thành công!"
                    return render(request,self.template_name,data)
                except:
                    data['error'] = "Điểm không hợp lệ, vui lòng nhập lại!"
                    return render(request,self.template_name,data)
        except:
            data['error'] = "Vui lòng nhập đầy đủ thông tin và nhập điểm hợp lệ"
            return render(request,self.template_name,data)