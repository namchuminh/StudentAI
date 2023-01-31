from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import InfoUser
from subjects.models import Subject
# Create your views here.

class Login(View):
    template_name =  'user/login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        
        return render(request,self.template_name)
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        
        if request.method == 'POST':
            username= request.POST["uname"]
            password = request.POST["psw"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_URL)
            else:
                result = {'error': 'Sai tài khoản hoặc mật khẩu! Vui lòng đăng nhập lại!'}     
                return render(request,self.template_name,result)

class Logout(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            logout(request)
            return redirect(settings.LOGOUT_URL)
        
        
class Home(View):
    template_name =  'user/home.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Home, self).dispatch(request, *args, **kwargs)
  
    def get(self, request, *args, **kwargs):
        
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        data = {
            'title': 'Trang Quản Trị - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
        }
        return render(request,self.template_name,data)


class Profile(View):
    template_name =  'user/profile.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Profile, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        subjects = Subject.objects.all().filter(infouser=infouser)

        data = {
            'title': 'Thông Tin Cá Nhân - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'address': infouser.address,
            'phone': infouser.phone,
            'birthday': infouser.birthday,
            'email': user.email,
            'active': user.is_active,
            'subjects': subjects
        }

        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.user.username
            old_pass= request.POST["old_pass"]
            new_pass = request.POST["new_pass"]
            confirm_pass = request.POST["confirm_pass"]
            
            user = User.objects.all().get(pk=request.user.pk)
            infouser = InfoUser.objects.all().get(user=user)
            subjects = Subject.objects.all().filter(infouser=infouser)
            
            data = {
                'title': 'Thông Tin Cá Nhân - StudentAI',
                'fullname': infouser.user.first_name + " " + infouser.user.last_name,
                'avatar': infouser.avatar,
                'specialization': infouser.specialization,
                'address': infouser.address,
                'phone': infouser.phone,
                'birthday': infouser.birthday,
                'email': user.email,
                'active': user.is_active,
                'subjects': subjects
            }
            
            user = authenticate(request, username=username, password=old_pass)
            if old_pass == "" or new_pass == "" or confirm_pass == "":
                data['error'] = "Vui lòng nhập đủ thông tin!"
                return render(request,self.template_name,data)
            elif user is None:
                data['error'] = "Mật khẩu cũ không đúng!"
                return render(request,self.template_name,data)
            elif new_pass != confirm_pass:
                data['error'] = "Mật khẩu mới nhập không trùng khớp!"
                return render(request,self.template_name,data)
            else:
                user.set_password(new_pass)
                user.save()
                data['success'] = "Thay đổi mật khẩu thành công!"
                return render(request,self.template_name,data)


            
            