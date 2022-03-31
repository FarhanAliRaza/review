import sys 
sys.path.append('..')

import  django
import os
os.environ["DJANGO_SETTINGS_MODULE"] = 'app.settings'
django.setup()
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from accounts.models import User
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator


# user = User.objects.get(slug='farhanmyslug')
# x = urlsafe_base64_encode(force_bytes(user.slug))
# tkn = default_token_generator.make_token(user)
# print(default_token_generator.check_token(user, tkn))

# print(x)
# print(force_text(urlsafe_base64_decode(x)))

def email_send(useremail, username, activation_link):

    subject = "Rawkana - User Activation Mail"
    html_message = render_to_string('rawkana/email-confirm.html', {'username': username, 'activation_link' : activation_link})
    plain_message = strip_tags(html_message)
    from_email = 'Rawkana <email@rawkana.com>'
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to = [useremail, ],
       

)
    email.content_subtype = "html"
    # try:
    email.send(fail_silently=False)
 


def email_forgot_send(useremail, username, activation_link):

    subject = "Rawkana - User Activation Mail"
    html_message = render_to_string('rawkana/password-request.html', {'username': username, 'activation_link' : activation_link})
    plain_message = strip_tags(html_message)
    from_email = 'Rawkana <email@rawkana.com>'
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to = [useremail, ],
       

)
    email.content_subtype = "html"
    # try:
    email.send(fail_silently=False)

# email_send('farhanalirazaazeemi@gmail.com', 'farhan', 'fb.com')
if __name__ == '__main__':
    email_send('farhanalirazaazeemi@gmail.com', 'test123', 'hello')