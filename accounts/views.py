from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.contrib import messages

User = get_user_model()

def login_user(request):
    if request.user.is_authenticated:        
        return redirect('audit')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('audit')
        else:
            messages.error(request, "Identifiant ou mot de passe incorrect !")
            return redirect('login')
        
    return render(request, 'accounts/login.html', {'title': 'Se connecté'})

def register_user(request):
    if request.user.is_authenticated:
        return redirect('audit')
    
    if request.method == "POST":
        company = request.POST.get("company")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if User.objects.filter(company=company):
            messages.error(request, "L'entreprise indiquer existe deja.")
            return redirect('register')
        
        if User.objects.filter(email=email):
            messages.error(request, "L'email indiquer existe deja.")
            return redirect('register')
        
        if User.objects.filter(username=username):
            messages.error(request, "Le nom d'utilisateur indiquer existe deja.")
            return redirect('register')
        
        if password != confirmpassword:
            messages.error(request, "Les deux mot de passe ne correspondent pas.")
            return redirect('register')
        
        my_company = User.objects.create_user(company=company, email=email, username=username, password=password) 
        my_company.save()
        messages.success(request, f"Un email de confirmation a ete envoyer a l'adresse: {email}")
        return redirect('register')
    
    return render(request, 'accounts/register.html', {'title': "S'inscrire"})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Vous avez ete bien deconnecté !')
        return redirect('login')
    
    return redirect('homepage')
