from django.shortcuts import render
from .forms import ConctactForm
from django.http import HttpResponse
from django.core.mail import send_mail                              
from django.conf import settings


# def contact(request):
#    """Show the page of contact with a Contact form with a API form"""
#    return render(request, "contact/contact.html")


def contact(request):                                                
    if request.method=="POST":                                                
        formdata= ConctactForm(request.POST)                                              
        if formdata.is_valid():                                                      
            data_valid= formdata.cleaned_data                             
            
            subject = data_valid["matter"]                                  
            message = data_valid["message"] + '/n Sended by: '+ data_valid['email']
            email_from = settings.EMAIL_HOST_USER                                   
            recipient_list = ['rocaedono@gmail.com'] 
            send_mail(subject, message, email_from, recipient_list)
            
            return render(request, "contact/contact_sended_mail.html")

        else:
            return HttpResponse("Form has a problem check again.")

    else:                                                                   
        formdata= ConctactForm()                                                          
        return render(request, "contact/contact.html", {'formulario': formdata}) 
    
    

