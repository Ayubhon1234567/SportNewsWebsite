from django.urls import path

from users.views import register_view, verify_email

app_name='users'

urlpatterns =[
    path('verify/email/',verify_email,name='verify-email '),
    path('register/',register_view,name='register')

]