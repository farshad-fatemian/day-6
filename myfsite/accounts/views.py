from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

# class RegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/register.html"
    
    
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form. 
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
 
        if form.is_valid():
            new_user = form.save()
        # Log in, redirect to home page.
            login(request, new_user)
            return redirect('product:product_list')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request,'registration/register.html', context)