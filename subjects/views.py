from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from students.models import Specialization
from subjects.models import Subject
from students.models import Students
from user.models import InfoUser

# Create your views here.
class ListSubjects(View):
    template_name =  'subjects/list.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(ListSubjects, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        
        if request.session['isStudent'] == True:
            user = User.objects.all().get(pk=request.user.pk)
            s = Students.objects.all().get(user=user)
            subjects = Subject.objects.all().filter(specialization=s.specialization)
            data = {
                'title': 'Trang Thông Tin Sinh Viên - StudentAI',
                'fullname': user.first_name + " " + user.last_name,
                'avatar': s.avatar,
                'specialization': s.specialization,
                'subjects': subjects,
            }
            return render(request,self.template_name,data)
        
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        subjects = Subject.objects.all().filter(infouser=infouser)
        
        data = {
            'title': 'Quản Lý Môn Học - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'subjects': subjects,
        }
        return render(request,self.template_name,data)


class CreateSubjects(View):
    template_name =  'subjects/create.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(CreateSubjects, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):

        if request.session['isStudent'] == True:
            return redirect('list_subjects')
        
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        specialization = Specialization.objects.all()
        
        data = {
            'title': 'Quản Lý Môn Học - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'specialization_list': specialization
        }
        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        if request.session['isStudent'] == True:
            return redirect('list_subjects')
        
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        specialization = Specialization.objects.all()
        
        data = {
            'title': 'Quản Lý Môn Học - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'specialization_list': specialization
        }
        
        if request.method == 'POST':
            subject_name = request.POST['subject_name']
            specialization_pk = request.POST['specialization']
            subject_credits = request.POST['subject_credits']
            
            if subject_name == "" or specialization_pk == "" or subject_credits == "":
                data['error'] = "Vui lòng nhập đầy đủ thông tin!"
                return render(request,self.template_name,data)
            else:
                specialization = Specialization.objects.all().get(pk=specialization_pk)
                
                subject = Subject(name=subject_name, credits=subject_credits, specialization=specialization, infouser=infouser)
                subject.save()
                
                data['success'] = "Thêm thông tin môn học thành công!"
                return render(request,self.template_name,data)

class UpdateSubjects(View):
    template_name =  'subjects/update.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(UpdateSubjects, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, pk, *args, **kwargs):
        if request.session['isStudent'] == True:
            return redirect('list_subjects')
        
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        subject = Subject.objects.all().get(pk=pk)
        specialization = Specialization.objects.all()
        
        credits = range(1, 6)
        
        data = {
            'title': 'Quản Lý Môn Học - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'subject': subject,
            'specialization_list': specialization,
            'credits': credits
        }
        return render(request,self.template_name,data)

    def post(self, request, pk, *args, **kwargs):
        if request.session['isStudent'] == True:
            return redirect('list_subjects')
        
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        subject = Subject.objects.all().get(pk=pk)
        specialization = Specialization.objects.all()
        
        credits = range(1, 6)
        
        data = {
            'title': 'Quản Lý Môn Học - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'subject': subject,
            'specialization_list': specialization,
            'credits': credits
        }
        
        subject_name = request.POST['subject_name']
        specialization_pk = request.POST['specialization']
        subject_credits = request.POST['subject_credits']
        subject_teaching = True if request.POST['subject_teaching'] == '1' else False
        
        if request.method == 'POST':
            
            if subject_name == "" or specialization_pk == "" or subject_credits == "" or subject_teaching == "":
                data['error'] = "Vui lòng nhập đầy đủ thông tin!"
                return render(request,self.template_name,data)

            try:
                subject = Subject.objects.all().get(pk=pk)
                specialization = Specialization.objects.all().get(pk=specialization_pk)

                subject.name = subject_name
                subject.credits = subject_credits
                subject.teaching = subject_teaching
                subject.specialization = specialization
                subject.save()
                
                data['subject'] = subject
                data['success'] = "Cập nhật thông tin môn học thành công!"
                data['credits'] = subject.credits
                return render(request,self.template_name,data)
            except:
                data['error'] = "Có lỗi khi cập nhật thông tin! Vui lòng thử lại!"
                return render(request,self.template_name,data)

                
    
