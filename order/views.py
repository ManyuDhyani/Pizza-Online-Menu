from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Pizza, About, Contact, Prizesize
from .filter import PizzaFilter
from .forms import SendmailForm
from Pizza.settings import EMAIL_HOST_USER

def index(request):
    about = About.objects.first()
    contact = Contact.objects.first()
    gallery = Pizza.objects.filter(gallery=True)[:6]
    offer = Pizza.objects.filter(offer=True)[:2]
    sent = False
    if request.method == 'POST':
        form = SendmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name, message)
            Email = EMAIL_HOST_USER
            Subject = "name: " + name + " " + "email: " + email + "Subject: " + subject
            sent = send_mail(Subject, message, Email, [Email])
            sent = True if sent else False
            return redirect(reverse('index'))
    else:
        form = SendmailForm()
    context = {
        'about': about,
        'contact': contact,
        'gallery': gallery,
        'offer': offer,
        'form': form,
        'sent': sent
    }
    return render(request, 'index.html', context)


def menu(request):
    form = PizzaFilter(request.GET, queryset=Prizesize.objects.all())

    context = {
        'filter': form,
    }
    return render(request, 'menu.html', context)

def detail(request, slug):
    pizza = get_object_or_404(Pizza, slug=slug)
    prize_size = Prizesize.objects.filter(pizza=pizza)
    context = {
        'pizza': pizza,
        'prize': prize_size
    }
    return render(request, 'detail.html', context)