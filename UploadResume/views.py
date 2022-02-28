from django.shortcuts import render
from .models import *
from .forms import *
from django.core.exceptions import ValidationError

# Create your views here.
def UploadProfile(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
        #     #n1 = form.cleaned_data.get("fname")
        #     form.save()
        #     obj=form.instance
        #     form = ResumeForm()
        #     return render(request,"uploads/uploadprofile.html",{'form':form, "obj":obj})
            image = form.cleaned_data.get('photo')
            if image:
                if image.size > 150*1024:
                    raise ValidationError("Profile photo too large ( > 150kb )")
                else:
                    form.save()
                    obj=form.instance
                    form = ResumeForm()
                    return render(request,"uploads/index.html",{'form':form, "obj":obj})
            else:
                raise ValidationError("Please select profile photo")
        else:
            return render(request, "uploads/index.html", {'form':form})

    else:
        form = ResumeForm()
        return render(request, 'uploads/index.html', {'form':form})

def ViewProfiles(request):
    if request.method == 'GET':
        resumes = ResumeModel.objects.all()
        return render(request, 'uploads/viewprofiles.html', {'resumes' : resumes})

def Jobs(request):
    return render(request, 'uploads/jobs.html')

def Contact(request):
    return render(request, 'uploads/contact.html')
