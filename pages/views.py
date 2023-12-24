from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms

# Create your views here.

def login_view(request):
    if request.method == "GET":
        login_form = forms.Login()
        return render(request, 'login.html', { 'login_form': login_form })
    if request.method == "POST":
        user_info = request.POST
        form = forms.Login(user_info)
        if form.is_valid():
            user = authenticate(request, username=user_info["username"], password=user_info["password"])
            if user is not None:
                login(request, user)
                return redirect(index_view)
            else:
                messages.add_message(request, messages.ERROR, "The username and/or password seem to be incorrect. Please try again.")
                return redirect(login_view)
        else:
            messages.add_message(request, messages.ERROR, "The username and/or password seem to be incorrect. Please try agian.")
            return redirect(login_view)
    
def signup_view(request):
    if request.method == "GET":
        signup_form = forms.Signup()
        return render(request, 'signup.html', { 'signup_form': signup_form })
    if request.method == "POST":
        user_info = request.POST
        form = forms.Signup(user_info)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            messages.add_message(request, messages.SUCCESS, "User has been successfully created. You may now login.")
            return redirect(signup_view)
        else:
            error_string = getFormErrors(form)
            messages.add_message(request, messages.ERROR, mark_safe(error_string))
            return redirect(signup_view)

@login_required
def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    
@login_required
def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logout Successful!")
    return redirect(login_view)
    
def getFormErrors(form):
    errors = list(form.errors.values())
    error_string = "<u>ERROR(S):</u><br>"
    for i in range(len(errors)):
        error_string = error_string + str(list(form.errors.values())[i][0]) + "<br>"
    return error_string