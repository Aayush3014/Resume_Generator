from django.shortcuts import render
from .models import ProfileFields
# Create your views here.

def index(request):

    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        experience = request.POST.get("experience","")
        skills = request.POST.get("skills","")


        profile = ProfileFields(name=name,summary=summary,phone=phone,school=school,university=university,degree=degree,email=email,experience=experience,skills=skills)

        profile.save()    
    return render(request, "resume/index.html")

def resume(request, id):
    user_profile = ProfileFields.objects.get(id=id)
    return render(request,'resume/resume.html',{'user_profile':user_profile})