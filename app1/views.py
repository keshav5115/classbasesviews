from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
# Create your views here.
from .forms import userform

#-------------function based view-------------
def userview(request):
    form=userform()
    if request.method =='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data has stored')
    return render(request,'create.html',{'form':form})

#-----------class based views--------------------
class userclassview(View):
    
    def get(self,request):
        form=userform()
        return render(request,'create.html',{'form':form})
    
    def post(self,request):
        form=userform()
        if request.method =='POST':
            form=userform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('data has stored')

#-------function based view for updation-------

def userupdate(request,pk):
    data=User.objects.get(id=pk)
    form=userform(instance=data)
    if request.method=='POST':
        form=userform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponse('data updated')
    return render(request,'update.html',{'form':form})

#-----------class based view for updation----------

class userupdateview(View):
    def get(self,request,pk):
        data=User.objects.get(id=pk)
        form=userform(instance=data)
        return render(request,'update.html',{'form':form})
    

    def post(self,request,pk):
        data=User.objects.get(id=pk)
        if request.method=='POST':
            form=userform(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return HttpResponse('data updated')



#----------------class based view   for read--------------
class userreadview(View):
    def get(self,request):
        object=User.objects.all()
        return render(request,'read.html',{'object':object})




#-----------class based view for delete---------------------

class userdeleteview(View):
    def get(self,request,pk):
        object=User.objects.get(id=pk)
        return render(request,'delete.html',{'object':object})

    def post(self,request,pk):
        if request.method=='POST':
            object=User.objects.get(id=pk).delete()
            return HttpResponse('DATA IS DELETED')


#-------predefined  class based views   -----------


class createuserview(CreateView):
    model=User
    # form_class=userform
    fields=['username','first_name','last_name','email','password']
    # context_object_name='form'
    template_name='create.html'
    success_url='/cbread/'


#------predefined update view-------------------
class updateuserview(UpdateView):
    model=User
    form_class=userform
    template_name='update.html'
    success_url='/cbread/'

class listuserview(ListView):
    model=User
    context_object_name='data'
    template_name='list.html'

class detailuserview(DetailView):
    model=User
    context_object_name='data'
    template_name='detail.html'

class deleteuserview(DeleteView):
    model=User
    context_object_name='object'
    template_name='delete.html'
    success_url='/cbread/'