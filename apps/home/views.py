# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Profile, Course, Faculty


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Profile.objects.all()
    courses = Course.objects.all()
    faculties = Faculty.objects.all()

    # title_contains_query = request.GET.get('title_contains')
    course = request.GET.get('search_sub')
    faculty = request.GET.get('faculty')
    rate_min = request.GET.get('min_range')
    rate_max = request.GET.get('max_range')

    if is_valid_queryparam(course):
        qs = qs.filter(course__name=course)

    if is_valid_queryparam(faculty) and faculty != 'Select Faculty':
        qs = qs.filter(faculty__name=faculty)

    if is_valid_queryparam(rate_min):
        qs = qs.filter(rate__gte=rate_min)

    if is_valid_queryparam(rate_max):
        qs = qs.filter(rate__lte=rate_max)

    # if is_valid_queryparam(rate_max):
    #     qs = qs.filter(views__lt=rate_min)

    return qs

def index(request):
    qs = filter(request)
    context = {'segment': 'index',
               'queryset' : qs,
               'faculties': Faculty.objects.all(),
               'courses': Course.objects.all()}


    html_template = loader.get_template('home/homepage.html')
    return HttpResponse(html_template.render(context, request))



def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
