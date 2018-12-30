"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collection.backends import MyRegistrationView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from collection import views

urlpatterns = [
    path('accounts/register/', MyRegistrationView.as_view(),
        name="registration_register"),
    path('accounts/create_thing', views.create_thing,
        name="registration_create_thing"),

    path('', views.index, name='home'),
    path('about/',
    TemplateView.as_view(template_name='about.html'),
        name='about'),
    path('contact/',
    TemplateView.as_view(template_name='contact.html'),
        name='contact'),

    path('things/', RedirectView.as_view(
        pattern_name='browse', permanent=True)),
    path('things/<slug>/', views.thing_detail,
        name='thing_detail'),
    path('things/<slug>/edit/',
        views.edit_thing, name='edit_thing'),

    path('browse/', RedirectView.as_view(
        pattern_name='browse', permanent=True)),
    path('browse/name/', views.browse_by_name,
        name="browse"),
    path('browse/name/<initial>/', views.browse_by_name,
        name="browse_by_name"),

    path('accounts/password/reset', password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
    path('accounts/password/reset/done', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    path('accounts/password/done/', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    path('account/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
