from django.urls import path
from django.urls.conf import re_path
# from .views import login_view, logout_view, register_user, email_verify, verify_phone, phonecodeverify, change_pass, forgot_pass, forgot_change_pass, profile_view, resend_email, delete_profile
from .views import login_view, logout_view, register_user, activate_user, forgot_pass, forgot_change_pass


urlpatterns = [
    path('login/',  login_view),
    path('register/',  register_user),

    path('logout/', logout_view, name='logout'),
    path('forgot_pass/', forgot_pass, name='forgot'),
    path('activate_user/<str:id>/<str:token>/', activate_user, name='activate_user'),
    path('forgot_password/<str:id>/<str:token>/', forgot_change_pass, name='forgotchng'),


]


