from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request,'accounts/skills.html')
def signup(requst):
    fm = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': fm})

