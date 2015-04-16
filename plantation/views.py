from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from plantation.forms import UserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# def index(request):
#     return HttpResponse("THIS IS A PLANTATION app for the index!")
# def about(request):
#     return HttpResponse("I am the ABOUT PAGE!!!")

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am a god..Therefore I am bold"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'plantation/index.html', context_dict)

def register(request):
    if request.POST:
        print request.POST
        password = request.POST['password']
        username = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username, username, password, first_name=first_name, last_name=last_name)
        user.save()


    context_dict = {'boldmessage': "This is the register page"}

    return render(request, 'plantation/register.html', context_dict)

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'plantation/Map2.html')