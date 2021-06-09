from django.core import mail
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)
            mail.send_mail('Confirmação de inscrição',
                        body,
                        'contato@eventex.com.br',
                        ['contato@eventex.com.br', form.cleaned_data['email']])
            messages.success(request, 'Inscrição realizada com sucesso!')
            return redirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html', {'form': form})
    else:
        context = {"form": SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)


# Create your views here.
