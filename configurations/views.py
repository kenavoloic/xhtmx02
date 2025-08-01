from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'configurations/pages/login.html'
    redirect_authenticated_user = True

def tableau_de_bord(request):
    return render(request, 'configurations/pages/tableau.html')

def page_inconnue(request, exception):
    if request.user.is_authenticated:
        return redirect("tableau")
    else:
        return redirect("login")

# def accueil(request):
#     return render(request, 'accueil.html')

# def about(request):
#     return render(request, 'about.html')

# def services(request):
#     return render(request, 'services.html')

# def contact(request):
#     return render(request, 'contact.html')
    
