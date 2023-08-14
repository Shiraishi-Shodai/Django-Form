from django.shortcuts import render
from .forms import ContactForm, Test
from .models import *

def index(request):
    
    if request.method == 'POST':    #POST,GETは大文字でないと反応しない
        
        f = ContactForm(request.POST) #postで受け取ったデータを格納しfに代入
    else:
        #データを挿入
        f = ContactForm({
            'subject':'math',
            'message' : 'Hello World',
            'sender' : 'siracnosuke@gmail.com',
    })
    return render(request, 'index.html', {'form' : f})

def modelPut(request):
    # Device.objects.create(name="iphone13", place='130000', type='expensive')
    # device = Device.objects.all()
    # print(device)
    
    a = Test()
    return render(request, 'modelPut.html', {'test': a})