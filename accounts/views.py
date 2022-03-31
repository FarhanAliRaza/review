import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
import os
from accounts.models import User
# from .emailsend import email_send
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .emailsend import email_send, email_forgot_send

def login_view(request):
    form = LoginForm()
    msg = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            try:
                u = User.objects.get(email = email)
            except:
                messages.error(request, 'Authentication Error')
                return render(request, "login.html", {'form':form, })
            if not u.is_active:
                user = u
                messages.error(request, 'User is not activated')
                return render(request, "login.html", {'form':form,  })

            user = authenticate(email=email, password=password)
            if user is not None:
                # if user.is_active:
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                   ip = x_forwarded_for.split(',')[0]
                else:
                   ip = request.META.get('REMOTE_ADDR')
                
                login(request, user)
                user.ip = ip
                user.save()
                # email_sending.login(request.user.username, "Login Email", request.user.email, ip)
                return redirect("/")
            else:
                messages.error(request, 'Authentication Error')
                return render(request, "login.html", {'form':form, })
        else:
            msg = 'Error validating the form'
    return render(request, "login.html", {'form':form})

def logout_view(request):
    logout(request)
    return redirect("/accounts/login/")
           

def register_user(request):

   
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
       
            now = timezone.now()
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
               ip = x_forwarded_for.split(',')[0]
            else:
               ip = request.META.get('REMOTE_ADDR')
            user = User.objects.get(email=email)
            user.ip = ip
            email = user.email
            username = user.username
            idt = urlsafe_base64_encode(force_bytes(user.id))
            tkn = default_token_generator.make_token(user)
            link = f"https://app.rawkana.com/accounts/activate_user/{idt}/{tkn}/"
            email_send(email, username, link )
            messages.info(request, "Email sent. Check your email to activate your account")
           
            return redirect('/accounts/login/')
        else:
            print(form)
            return render(request, "register.html", {"form": form})

            
    else:
        form = SignUpForm()

# 
    return render(request, "register.html", {"form": form})





def forgot_pass(request):
  
    if request.method == "POST":
        
        if "rrrr" in request.session:
            retries = request.session["rrrr"]
            print(retries)
            request.session["rrrr"] = str(int(retries) + 1)
            if int(request.session["rrrr"]) > 3:
                return HttpResponse("Retry Limit Reached. Retry Later")
        else:
            request.session["rrrr"] = "1"
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user != None :
            del request.session["rrrr"]
            slg = urlsafe_base64_encode(force_bytes(user.id))
            tkn = default_token_generator.make_token(user)
            link = f"https://app.rawkana.com/accounts/forgot_password/{slg}/{tkn}/"
            user.save()
            email_forgot_send(useremail=user.email, username=user.username, activation_link=link)
            messages.info(request, "Email sent. Please check your email")
            return redirect('/accounts/login/')
        messages.info(request, "User does not exist")
        return render(request, 'forgot_pass.html', {})

    return render(request, 'forgot_pass.html', {'normal': True})



def activate_user(request, id, token):
    try:

        idt = force_text(urlsafe_base64_decode(id))
        user = User.objects.get(id=idt)
        if not default_token_generator.check_token(user, token):
            return HttpResponse("Your Link is Expired")
    except:
        user = None
    if user != None:
        user.is_active = True
        user.save()
        messages.info(request, "Your acount is activated")
        return redirect('/accounts/login/')
    else:
        return redirect('/accounts/login/')



def forgot_change_pass(request, id, token):
    try:
        idt = force_text(urlsafe_base64_decode(id))
        user = User.objects.get(id=idt)
        if not default_token_generator.check_token(user, token):
            return HttpResponse("Your Link is Expired")
    except:
        user = None
    
    if request.method == "POST" and user != None:
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            user.set_password(pass1)
            user.save()
            messages.info(request, "Password changed")
            return redirect('/accounts/login/')
        else:
            messages.info(request, "Password does not match!")
            return render(request, 'forgot_change_pass.html', {'normal': True})
    if user != None:
        return render(request, 'forgot_change_pass.html', {'normal': True})
    else:
        return redirect('/accounts/login/')

 



    

# def resend_email(request, slug):
#     now = timezone.now()

#     user = User.objects.get(slug=slug)
#     # slug = utils.unique_key_generator(user)
#     # user.slug = slug
#     # user.save()
#     user.email_ac_timestamp = now
#     user.save()
#     link = f"https://app.bulkmailverifier.com/accounts/email/activate/{user.slug}"
#     email = user.email
#     username = user.username
#     try:
#         email_send(useremail=email, username=username, activation_link=link)
#     except Exception as e:
#         print(e)
#         messages.error(request, 'Something Went wrong.')
#         return redirect("/accounts/login/")

#     messages.info(request, 'Email is sent check your email adresss')
#     return redirect("/accounts/login/")


# def email_verify(request, slug):
#     try:
#         user = User.objects.get(slug=slug)

#     except:
#         pass
#     if user:
#         if user.is_active:
#             login(request, user)
#             return redirect("/")
#             # return("User is already active")
#         else:
#             now = timezone.now()

#             pt = user.email_ac_timestamp
#             print(now)
#             print(pt)
#             td = now - pt
#             if td > datetime.timedelta(days=1):
#                 return HttpResponse("Email time has passed <button>Resend Email</button>")
#             user.is_active = True
#             user.save()
#             return redirect("/accounts/")


# @login_required
# def change_pass(request):
#     form = Change_Password_Form()
#     if request.method == "POST":
#         form = Change_Password_Form(request.POST)
#         print(form)
#         if form.is_valid():
#             pass1 = form.cleaned_data.get("password1")
#             pass2 = form.cleaned_data.get("password2")
#             if pass1 != pass2:
#                 return render(request, 'changepassword.html', {'form' : form, 'is_error': True })
#             request.user.set_password(pass1)
#             request.user.save()
#             return redirect("/")
            
#     return render(request, 'changepassword.html', {'form' : form})






# def forgot_change_pass(request, slug, token):
#     try:

#         slg = force_text(urlsafe_base64_decode(slug))
#         user = User.objects.get(slug=slg)
#         if not default_token_generator.check_token(user, token):
#             return HttpResponse("Your Link is Expired")




#     except:
#         user = None
#     if user != None:
#             now = timezone.now()
#             pt = user.email_ac_timestamp
#             print(now)
#             print(pt)
#             td = now - pt
#             if td > datetime.timedelta(days=1):
#                 return HttpResponse("Your Link is Expired")
#             form = Change_Password_Form()
#             if request.method == "POST":
#                 form = Change_Password_Form(request.POST)
#                 print(form)
#                 if form.is_valid():
#                     pass1 = form.cleaned_data.get("password1")
#                     pass2 = form.cleaned_data.get("password2")
#                     if pass1 != pass2:
#                         return render(request, 'changepassword.html', {'form' : form, 'is_error': True })
#                     user.set_password(pass1)
#                     user.save()
#                     return redirect("/")

#             return render(request, 'changepassword.html', {'form' : form})
# @login_required
# def profile_view(request):
#     if not request.user.is_phone:
#         return redirect('/accounts/phone-verify/')
#     if request.method == "POST":
#         try:
#             pass1 = request.POST.get('password')
#             pass2 = request.POST.get('repassword')
#         except:
#             pass
#         if pass1 != '':
#             if pass1 == pass2:
#                 request.user.set_password(pass1)
#                 request.user.save()
#                 update_session_auth_hash(request, request.user)  # Important!
#                 return render(request, 'profile.html', {'email' : request.user.email, 'username' : request.user.username, 'phone' : request.user.phone, 'message' : 'Your password was changed successfully'  })
#             else:
#                 return render(request, 'profile.html', {'email' : request.user.email, 'username' : request.user.username, 'phone' : request.user.phone, 'error' : True })

#         else:
#             usr = request.POST.get('username')
#             if usr == request.user.username:
#                 return render(request, 'profile.html', {'email' : request.user.email, 'username' : request.user.username, 'phone' : request.user.phone})
#             else:
#                 request.user.username = usr
#                 request.user.save()
#                 return render(request, 'profile.html', {'email' : request.user.email, 'username' : request.user.username, 'phone' : request.user.phone, 'message' : 'Your username was changed successfully'  })
#     return render(request, 'profile.html', {'email' : request.user.email, 'username' : request.user.username, 'phone' : request.user.phone })
# @login_required
# def delete_profile(request):
#     if not request.user.is_phone:
#         return redirect('/accounts/phone-verify/')
#     user = request.user
#     d =  DelUser.objects.create(email = user.email, phone = user.phone)
#     # user.delete()
#     user.email = None
#     user.phone = None
#     user.del_user = d
#     user.is_active = False
#     user.is_phone = False
#     user.save()
#     logout(request)
#     return redirect('/')
    