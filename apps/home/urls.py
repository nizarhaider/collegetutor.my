# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.conf.urls.static import static
from .views import ChangePasswordView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # profile page
    path('tutor', views.profile, name='tutor'),

    path('password-change', ChangePasswordView.as_view(), name='password_change')

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
