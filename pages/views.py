from django.shortcuts import render, redirect
from django.conf import settings
from .models import MerchItem


def home(request):
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        if profile and not profile.questionnaire_completed:
            return redirect('accounts:questionnaire')
        if profile and profile.questionnaire_completed:
            from exercises.models import Exercise
            from faq.models import FAQ
            exercises = Exercise.objects.filter(
                diagnosis=profile.diagnosis,
                pain_level_min__lte=profile.pain_level,
                pain_level_max__gte=profile.pain_level,
            )[:6]
            faqs = FAQ.objects.filter(diagnosis=profile.diagnosis)[:5]
            return render(request, 'pages/home.html', {
                'profile': profile,
                'exercises': exercises,
                'faqs': faqs,
            })
    return render(request, 'pages/home_guest.html')


def telehealth(request):
    return render(request, 'pages/telehealth.html', {
        'calendly_url': settings.CALENDLY_URL,
    })


def merch(request):
    items = MerchItem.objects.filter(active=True)
    return render(request, 'pages/merch.html', {'items': items})


def about(request):
    return render(request, 'pages/about.html')
