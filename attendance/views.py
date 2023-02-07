from django.shortcuts import render, redirect
from django.views import View
from user.models import InfoUser
from django.contrib.auth.models import User
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from django.conf import settings
import os, shutil
import cv2
import uuid
from students.models import ClassName, Students

def stream():
    cap = cv2.VideoCapture(0) 
    
    global frame, x, y, w, h

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: failed to capture image")
            break
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        for (x, y, w, h) in cv2.CascadeClassifier(os.path.join(settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml')).detectMultiScale(gray_img, 1.1, 9):
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        cv2.imwrite(os.path.join(settings.BASE_DIR,'media/video_stream/demo.jpg'), frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open(os.path.join(settings.BASE_DIR,'media/video_stream/demo.jpg'), 'rb').read() + b'\r\n')
        

def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')


class Attendance(View):
    template_name =  'attendance/attendance.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Attendance, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        data = {
            'title': 'Điểm Danh Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
        }
        
        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        data = {
            'title': 'Điểm Danh Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
        }
        
        folder = os.path.join(settings.BASE_DIR,'media/face_attendance/')
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        
        
        img = frame[y + 2:y + h - 2, x + 2:x + w-2]
        
        img_name = str(uuid.uuid4())
        
        cv2.imwrite(os.path.join(settings.BASE_DIR,'media/face_attendance/'+img_name+'.jpg'), img)

        data['face'] = '/media/face_attendance/'+img_name+'.jpg'
        
        return HttpResponse(data['face'])

class CropFace(View):
    template_name =  'attendance/cropface.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(CropFace, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        classname = ClassName.objects.all()
        
        data = {
            'title': 'Thêm Khuân Mặt Điểm Danh Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'classname': classname
        }
        
        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        
        print(request.POST)
        
        if len(request.POST) == 3:
            try:
                img = frame[y + 2:y + h - 2, x + 2:x + w-2]
                    
                img_name = str(uuid.uuid4())
                if not os.path.exists(os.path.join(settings.BASE_DIR,'media/face_students/'+request.POST['student']+'/')):
                    os.makedirs(os.path.join(settings.BASE_DIR,'media/face_students/'+request.POST['student']+'/'))
                    cv2.imwrite(os.path.join(settings.BASE_DIR,'media/face_students/'+request.POST['student']+'/'+img_name+'.jpg'), img)
                else:
                    cv2.imwrite(os.path.join(settings.BASE_DIR,'media/face_students/'+request.POST['student']+'/'+img_name+'.jpg'), img)
                
                return HttpResponse("1")
            except:
                return HttpResponse("0")
        
        if request.POST['classname'] is not None:
            
            classname = ClassName.objects.all().get(pk=request.POST['classname'])
            
            students = Students.objects.all().filter(classname=classname).values('pk','fullname')
            
            data = list(students)
            
            return JsonResponse({'data': data})
        
        