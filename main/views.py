from django.shortcuts import render, redirect
from .models import Contacts, Services
from django.contrib import messages 

# Create your views here.

# Home page 
def home(request):

    # Getting user input from the webpage 
    if request.method == 'POST':
        pass


    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')



def contact(request):

    if request.method =='POST':
        try:
            name = request.POST['name']
            email = request.POST['Email']
            subject = request.POST['subject']
            message = request.POST['message']

            contact = Contacts.objects.create(name=name, email=email, message=message, subject=subject)
            contact.save()

            messages.info(request, "Thank you for contacting Us, We'll get ack to you shortly")
            return redirect('home')
        except:
            messages.info(request, "An error occured while sending request")
            return redirect('contact')

    return render(request, 'contact.html')



def services(request):
    services = Services.objects.all()
    return render(request, 'serve.html', {'services': services} )


