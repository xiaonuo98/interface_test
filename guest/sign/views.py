from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    #return HttpResponse("hello django")
    return render(request,"index.html")

#发布会管理
def event_manage(request):
    return render(request,"event_manage.html")

#登录动作
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        #username=request.post.get（'username','')
        password=request.POST.get('password','')
        if username=='admin' and password=='123':
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,'index.html',{'error':'username or password error'})
