from django.shortcuts import render, redirect
from django.views import View
from user.models import InfoUser
from .models import AttendanceInfo
from django.contrib.auth.models import User
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from django.conf import settings
import os, shutil
import cv2
from datetime import date
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from keras.models import load_model  # TensorFlow is required for Keras to work
import uuid
from students.models import ClassName, Students
from subjects.models import Subject, Specialization

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
        
        subject = Subject.objects.all()
        
        data = {
            'title': 'Điểm Danh Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'subject': subject
        }
        
        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        
        if len(request.POST) == 2:
            specialization = Specialization.objects.all().get(pk=request.POST['specialization'])
            
            classname = ClassName.objects.all().filter(specialization=specialization).values('pk', 'name')
            
            data = list(classname)
            
            return JsonResponse({'data': data})
        
        
        try:
            
            user = User.objects.all().get(pk=request.user.pk)
            infouser = InfoUser.objects.all().get(user=user)
            
            data_res = {
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

            data_res['face'] = '/media/face_attendance/'+img_name+'.jpg'

            # Disable scientific notation for clarity
            np.set_printoptions(suppress=True)

            # Load the model
            model = load_model(os.path.join(settings.BASE_DIR,"model/keras_Model.h5"), compile=False)

            # Load the labels
            class_names = open(os.path.join(settings.BASE_DIR,"model/labels.txt"), "r").readlines()

            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            # Replace this with the path to your image
            image = Image.open(os.path.join(settings.BASE_DIR,'media/face_attendance/'+img_name+'.jpg')).convert("RGB")

            # resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

            # turn the image into a numpy array
            image_array = np.asarray(image)

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # Predicts the model
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            student_pk = class_name[2:]
            
            print(student_pk)
            
            try:
                s = Students.objects.all().filter(pk=student_pk).values('pk', 'fullname', 'birthday', 'gender', 'classname__name', 'avatar')
                data = list(s)
                
                
                classname = ClassName.objects.all().get(pk=request.POST['classname'])
                
                subject = Subject.objects.all().get(pk=request.POST['subject'])
                
                student = Students.objects.all().get(pk=student_pk, classname=classname)
                
                attendance_infos_check = AttendanceInfo.objects.all().filter(student=student, classname=classname, subject=subject, date = date.today()).count()
                
                if(attendance_infos_check == 1):
                    return HttpResponse('check')
                else:
                    attendance_infos = AttendanceInfo(student=student, classname=classname, subject=subject)
                    attendance_infos.save()
                        
                    return JsonResponse({'data': data})
            except:
                return HttpResponse('false')
        except:
            return HttpResponse('false')
        

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
        

class AttendanceInformation(View):
    template_name =  'attendance/attendanceinfo.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(AttendanceInformation, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=request.user.pk)
        infouser = InfoUser.objects.all().get(user=user)
        
        subject = Subject.objects.all()
        
        data = {
            'title': 'Thông Tin Điểm Danh Sinh Viên - StudentAI',
            'fullname': infouser.user.first_name + " " + infouser.user.last_name,
            'avatar': infouser.avatar,
            'specialization': infouser.specialization,
            'subject': subject
        }
        
        return render(request,self.template_name,data)
    
    def post(self, request, *args, **kwargs):
        
        if len(request.POST) == 4:
            
            classname = ClassName.objects.all().get(pk=request.POST['classname'])
            
            student = Students.objects.all().filter(classname=classname).values('pk','fullname', 'classname__name', 'specialization__name', 'birthday', 'avatar')
            
            subject = Subject.objects.all().get(pk=request.POST['subject'])
            attendanceinfo = AttendanceInfo.objects.all().filter(classname=classname, subject=subject, date=request.POST['date']).values('student__pk')
            
            data_student = list(student)
            data_attendanceinfo = list(attendanceinfo)
            return JsonResponse({'data': {"data_student" : data_student, "data_attendanceinfo": data_attendanceinfo}})
        
        if len(request.POST) == 2:
            specialization = Specialization.objects.all().get(pk=request.POST['specialization'])
            
            classname = ClassName.objects.all().filter(specialization=specialization).values('pk', 'name')
            
            data = list(classname)
            
            return JsonResponse({'data': data})