from django.shortcuts import redirect,render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('notes.list')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().post(request, *args, **kwargs)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'home/logout.html')

class LoginINterfaceView(LoginView):
    template_name = 'home/login.html'
    



class HomeView(TemplateView):
    template_name = 'home/index.html'


    
