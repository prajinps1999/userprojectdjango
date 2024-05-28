from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import User
from .models import Portfolio
def index(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def list(request):
        return render(request, 'list.html')
def user(request):
    users = User.objects.all()
    if request.method == 'POST':
        bio = request.POST.get('bio')
        skill_set = request.POST.get('skill_set')
        contact_details = request.POST.get('contact_details')
        user= User(bio=bio, skill_set=skill_set, contact_details=contact_details)
        user.save()
    return render(request, 'user.html',{'users':users})

def detailuser(request,user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'detailuser.html', {'user': user})

def updateuser(request,user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        skill_set = request.POST.get('skill_set')
        contact_details = request.POST.get('contact_details')

        user.bio = bio
        user.skill_set = skill_set
        user.contact_details = contact_details

        user.save()
        return redirect('/')
    return render(request, 'updateuser.html', {'user': user})

def deleteuser(request,user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('/')
    return render(request, 'deleteuser.html', {'user': user})