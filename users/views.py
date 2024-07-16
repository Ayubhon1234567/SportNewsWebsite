import random

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from conf import settings
from pages.models import ConfirmationModel
from users.forms import RegistrationForm

UserModel = get_user_model()


# Create your views here.


def send_activation_email(email):
    subject = 'Activation code'
    code = str(random.randint(100, 9999))
    sender = settings.EMAIL_HOST_USER
    recipient_list = [email]
    if send_mail(subject, code, sender, recipient_list):
        ConfirmationModel.objects.create(
            email=email,
            code=code
        )
        return True
    return False


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.data)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password2'])
            new_user.is_active = False
            new_user.save()

            if send_activation_email(form.cleaned_data['email']):
                # send code via email
                return render(request, 'registrations/verify-email.html')
            else:
                return HttpResponse(f"Something went wrong please try again")
    else:
        return render(request, 'registrations/user-register.html')


def verify_email(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        email = ConfirmationModel.object.filter(code=code).filter()
        if email:
            UserModel.objects.update(is_active=True)
            email.delete()
            return redirect('/')
        else:
            return HttpResponse('There is this kind of code')



