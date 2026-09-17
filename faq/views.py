from django.shortcuts import render
from .models import FAQ
from accounts.models import Diagnosis


def faq_list(request):
    faqs = FAQ.objects.select_related('diagnosis').all()

    search = request.GET.get('q', '').strip()
    diagnosis_slug = request.GET.get('diagnosis', '')

    if search:
        faqs = faqs.filter(question__icontains=search) | faqs.filter(answer__icontains=search)
    if diagnosis_slug:
        faqs = faqs.filter(diagnosis__slug=diagnosis_slug)

    diagnoses = Diagnosis.objects.all()

    return render(request, 'faq/list.html', {
        'faqs': faqs,
        'diagnoses': diagnoses,
        'search': search,
        'selected_diagnosis': diagnosis_slug,
    })
