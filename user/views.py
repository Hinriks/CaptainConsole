from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate 
from product.views import homepage
from product.urls import urlpatterns
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def view_profile(request):
    #TODO
    
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)

def edit_profile(request):
    user = request.user
    context= {'user': user}
    return render(request, 'edit_profile.html', context)

def signup_view(request):
    loginform = AuthenticationForm()
    form = SignUpForm(request.POST)
    print(form.errors)
    if form.is_valid():
        user = form.save()
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        login(request, user)
        print('form is valid')
        return redirect('homepage')
    else:
        print('form is not valid')
        form = SignUpForm()
        context = {'form': form, 'loginform':loginform}
    return render(request, 'registration/signup_general.html', context)


    

