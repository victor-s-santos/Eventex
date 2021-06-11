from django.conf import settings
from django.core import mail
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from django.template.loader import render_to_string

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    #send email
    _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'], 'subscriptions/subscription_email.txt',
                form.cleaned_data)

    Subscription.objects.create(**form.cleaned_data)
    #success feedback
    messages.success(request, 'Inscrição realizada com sucesso!')
    return redirect('/inscricao/')
        

def new(request):
    context = {"form": SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
# Create your views here.
