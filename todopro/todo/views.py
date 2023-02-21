from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.views import LoginView

# Create your views here.


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname=request.POST['fname']
        lname = request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"You created an account!")

        return redirect('login')

    return render(request,'signup.html')


class CustomLogin(LoginView):
    template_name='login.html'
    fields ='__all__'
    success_url = reverse_lazy('item')
    redirected_authenticated_user=True

    def get_success_url(self):
        return self.success_url


class Tasklist(ListView):
    model = Task
    context_object_name = 'item'
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('item')
    template_name = 'taskcreate.html'


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    context_object_name = 'item'
    success_url = reverse_lazy('item')
    template_name = 'taskcreate.html'


class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    context_object_name = 'item'
    success_url = reverse_lazy('item')
    template_name = 'delete.html'


class TaskDetailView(DetailView):
        model = Task
        fields='__all__'
        success_url = reverse_lazy('item')
        template_name = 'details.html'



