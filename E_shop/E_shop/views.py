from django.shortcuts import render,redirect

def base(request):
    return render(request,template_name='main/base.html')