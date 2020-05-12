from django.shortcuts import render


# Create your views here.
def view_profile(request):
    #TODO
    return render(request, 'profile/index.html')
