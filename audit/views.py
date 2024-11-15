from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import DomainPreference
from .func import *


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard/index.html', {'title': 'Audit'})

def scanning(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        messages.error(request, "Méthode de requête non autorisée.")
        return redirect('audit')
    domain = request.GET.get('domain', None)
    if domain:
        if checkIfDomainIsValid(domain):
            domain_info = getDomainInfos(domain)
            context = {
                'show' : True,
                'domain': domain_info['domain'],
                'value': True,
                'scan_result': True,
            }
            messages.success(request, f"L'analyse est terminer.")
            # context = context.pop('show')
            return render(request, 'dashboard/index.html', {'context' : context})
        else:
            messages.error(request, "Le domaine que vous avez spécifié est : <b>INDISPONIBLE !</b>")
    else:
        messages.error(request, "Aucun domaine spécifié.")
    return render(request, 'dashboard/index.html', {'title': 'Audit'})

def View404(request, exception):
    return render(request, 'errors/404.html', {}, status=404)


context = {'scan_result': True,}

def informations(request):
    if not request.user.is_authenticated:
        return redirect('login')    
    return render(request, 'dashboard/informations.html', {'context' : context, 'title': 'Information'})

def ports(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard/ports.html', {'context' : context, 'title': 'Ports'})

def vulnerability(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard/vulnerability.html', {'context' : context, 'title': 'Vulnerability'})

def repport(request):
    if not request.user.is_authenticated:
        return redirect('login')
    messages.success(request, "Telechargement du rapport de réussi.")
    return redirect('informations')
