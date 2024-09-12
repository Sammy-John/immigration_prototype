from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def send_new_user_email(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    email_subject = 'Welcome to the Immigration Prototype System'
    email_body = render_to_string('auth_app/new_user_email.html', {
        'user': user,
        'uid': uid,
        'token': token,
    })
    send_mail(email_subject, email_body, 'admin@yourdomain.com', [user.email])