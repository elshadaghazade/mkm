from django.shortcuts import render, redirect, reverse, get_object_or_404
from company_app.models import Companies
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.db.models import Q
from .models import *


# Create your views here.
def contact_main(request):
    context = {}
    if request.method == 'GET':
        form = ContactForm()
        context['form'] = form
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            body = form.cleaned_data['body']
            try:
                email = EmailMessage(subject_as_name,
                                     message,
                                     from_email,
                                     ['cavidan.hasanli@mail.ru',],
                                     headers={'Reply-To': from_email})
                email.send()
                context['form'] = form
                # Saving to database
                form.save()
                # Giving success message
                messages.success(request, 'Sizin məktubunuz uğurla göndərildi!')
                #TODO: change and give correct url after organising the project.
                return HttpResponseRedirect("")
                #return render(request, "contact.html", context)
                #TODO: margogngn@gmail.com yerine tehsil nazirliyinin mailini qoyaciq.
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "contact_main.html", context)


def contact_company(request,pk):
    context = {
        'company':get_object_or_404(Companies, pk=pk),
        'company_id':pk,
        'company_contact_model': ContactCompany,
        'address': ContactCompany.objects.filter(Q(company=pk) &  Q(contact_type=ContactCompany.CONTACT_TYPE_ADDRESS)),
        'contacts': ContactCompany.objects.filter(~Q(contact_type=ContactCompany.CONTACT_TYPE_ADDRESS), company=pk),
        'contact_form': ContactCompanyForm.objects.get(pk=pk)
    }
    
    return render(request, "contact_company.html", context)
