import email
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse
from user.models import InfoUser
from subjects.models import Subject
from .models import ClassName, Specialization, Students
from .forms import StudentsForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import xlwt
from django.db.models.functions import Cast
from django.db.models import TextField
import random
from django.contrib.auth.hashers import make_password

# Create your views here.
class ListStudents(View):
    template_name =  'students/list.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(ListStudents, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        students = Students.objects.all().filter(status=True)
        
        classname = ClassName.objects.all()

        data = {
            'title': 'Quản Lý Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'students': students,
            'classname': classname
        }
        return render(request,self.template_name,data)

    def post(self, request, *args, **kwargs):
        
        if len(request.POST) == 3:
            fullname = request.POST['search']
            
            students = Students.objects.all().filter(fullname__icontains=fullname, status=True).values('pk','fullname','birthday','gender','classname__name','address','avatar','phone','specialization__name').order_by('pk')
            
            data = list(students)
            
            return JsonResponse({'data': data})
        
        if request.POST['classnamepk'] is not None:
            classnamepk = request.POST['classnamepk']
            classname = ClassName.objects.all().get(pk=classnamepk)
            students = Students.objects.all().filter(classname=classname, status=True).values('pk','fullname','birthday','gender','classname__name','address','avatar','phone','specialization__name')

            data = list(students)

            return JsonResponse({'data': data})

class CreateStudents(View):
    template_name =  'students/create.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(CreateStudents, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        classname = ClassName.objects.all()
        
        specialization_all = Specialization.objects.all()
        
        data = {
            'title': 'Quản Lý Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'classname': classname,
            'specialization_all': specialization_all
        }
        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        classname = ClassName.objects.all()
        
        specialization_all = Specialization.objects.all()
        
        data = {
            'title': 'Quản Lý Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'classname': classname,
            'specialization_all': specialization_all
        }
        
        
        if len(request.POST) == 2:
            specializationpk = request.POST['specializationpk']
            
            specialization = Specialization.objects.all().get(pk=specializationpk)
            
            classname = ClassName.objects.all().filter(specialization=specialization).values('pk','name')
            
            data = list(classname)
    
            return JsonResponse({'data': data})
    
    
        if len(request.POST) == 10:
            myfile = request.FILES['avatar']
            fs = FileSystemStorage()
            fs.save('students/' + myfile.name, myfile)
            avatar = 'students/' + myfile.name
            
            if request.POST['first_name'] == "" or request.POST['last_name'] == "" or request.POST['gender'] == "" or request.POST['birthday'] == "" or request.POST['specialization'] == "" or request.POST['classname'] == "" or request.POST['address'] == "" or request.POST['phone'] == "":
                data["error"] = "Vui lòng nhập đầy đủ thông tin!"
                return render(request,self.template_name,data)
            else:
                username = "208103" + str(random.randint(10000, 99999))
                password = make_password(username, salt=None, hasher='default')
                usr = User(
                    username = username,
                    password = password,
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name']
                )
                usr.save()
                
                user = User.objects.all().get(username=username)
                classname = ClassName.objects.all().get(pk=request.POST['classname'])
                specialization = Specialization.objects.all().get(pk=request.POST['specialization'])
                s = Students(
                    user = user,
                    fullname = request.POST['first_name'] + ' ' + request.POST['last_name'], 
                    birthday = request.POST['birthday'],
                    gender = True if request.POST['gender'] == "1" else False,
                    specialization = specialization,
                    classname = classname,
                    address = request.POST['address'],
                    avatar = avatar,
                    phone = request.POST['phone']
                )
                s.save()
                
                data["success"] = "Thêm thông tin sinh viên thành công!"
                return render(request,self.template_name,data)
        else:
            data["error"] = "Vui lòng nhập đầy đủ thông tin!"
            return render(request,self.template_name,data)


class UpdateStudents(View):
    template_name =  'students/update.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(UpdateStudents, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, pk, *args, **kwargs):

        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        classname = ClassName.objects.all()
        
        data = {
            'title': 'Quản Lý Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'classname': classname,
        }
        
        try:
            student = Students.objects.all().get(pk=pk)
            data['student'] = student
            data['first_name'] = student.fullname.split(' ')[0] + ' ' + student.fullname.split(' ')[1] 
            data['last_name'] = student.fullname.split(' ')[2] 
            data['birthday'] = str(student.birthday)

            return render(request,self.template_name,data)
        except:
            return redirect('list_students')
    
    def post(self, request, pk, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        classname = ClassName.objects.all()
        
        specialization_all = Specialization.objects.all()
        
        data = {
            'title': 'Quản Lý Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'classname': classname,
            'specialization_all': specialization_all,
            
        }
        try:
            student = Students.objects.all().get(pk=pk)
            data['student'] = student
            data['first_name'] = student.fullname.split(' ')[0] + ' ' + student.fullname.split(' ')[1] 
            data['last_name'] = student.fullname.split(' ')[2] 
            data['birthday'] = str(student.birthday)

            if request.POST['first_name'] == "" or request.POST['last_name'] == "" or request.POST['gender'] == "" or request.POST['birthday'] == "" or request.POST['address'] == "" or request.POST['phone'] == "":
                data["error"] = "Vui lòng nhập đầy đủ thông tin!"
                return render(request,self.template_name,data)
                
            
            if len(request.POST) == 8:
                myfile = request.FILES['avatar']
                fs = FileSystemStorage()
                fs.save('students/' + myfile.name, myfile)
                avatar = 'students/' + myfile.name
                
                s = Students.objects.all().get(pk=pk)
                s.fullname = request.POST['first_name'] + ' ' + request.POST['last_name']
                s.birthday = request.POST['birthday']
                s.gender = True if request.POST['gender'] == "1" else False
                s.address = request.POST['address']
                s.avatar = avatar
                s.phone = request.POST['phone']
                s.save()
                
                data['student'] = s
                data['first_name'] = s.fullname.split(' ')[0] + ' ' + s.fullname.split(' ')[1] 
                data['last_name'] = s.fullname.split(' ')[2] 
                data['birthday'] = str(s.birthday)
                
                data["success"] = "Cập nhật thông tin sinh viên thành công!"
                return render(request,self.template_name,data)
            else:
                s = Students.objects.all().get(pk=pk)
                s.fullname = request.POST['first_name'] + ' ' + request.POST['last_name']
                s.birthday = request.POST['birthday']
                s.gender = True if request.POST['gender'] == "1" else False
                s.address = request.POST['address']
                s.phone = request.POST['phone']
                s.save()
                
                data['student'] = s
                data['first_name'] = s.fullname.split(' ')[0] + ' ' + s.fullname.split(' ')[1] 
                data['last_name'] = s.fullname.split(' ')[2] 
                data['birthday'] = str(s.birthday)
                
                data["success"] = "Cập nhật thông tin sinh viên thành công!"
                return render(request,self.template_name,data)
        except:
            return redirect('list_students')    

class Delete_Students(View):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Delete_Students, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, pk, *args, **kwargs):
        try:
            s = Students.objects.all().get(pk=pk)
            s.status = False
            s.save()
            return redirect('list_students')
        except:
            return redirect('list_students')
        
def export_students_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="SinhVien.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('SinhVien')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['MSSV', 'Họ Tên', 'Lớp Học', 'Chuyên Ngành', 'Ngày Sinh', 'Số Điện Thoại', 'Địa Chỉ']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Students.objects.all().values_list('pk','fullname', 'classname__name', 'specialization__name', 'birthday','phone','address').order_by('pk')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response