from django.shortcuts import render
from . import cam
# Create your views here.
from django.http import HttpResponse         #需要导入HttpResponse模块
from django.http import JsonResponse
def hello(request):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    return render(request,"log.html")    #不能直接字符串，必须是由这个类封装，此为Django规则
def index(request):
    return render(request,'index.html')
def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
                b'Conten-Type:image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')
def video_feed(request):
    return HttpResponse(gen(cam.VideoCamera()),
                        content_type='multipart/x-mixed-replace; boundary=frame')
