from django.shortcuts import render


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