from django.shortcuts import render, get_object_or_404
from .models import Exercise
from accounts.models import Diagnosis


def exercise_list(request):
    exercises = Exercise.objects.select_related('diagnosis').all()

    diagnosis_slug = request.GET.get('diagnosis')
    phase = request.GET.get('phase')
    pain = request.GET.get('pain')

    if diagnosis_slug:
        exercises = exercises.filter(diagnosis__slug=diagnosis_slug)
    if phase:
        exercises = exercises.filter(phase=phase)
    if pain:
        try:
            pain_val = int(pain)
            exercises = exercises.filter(
                pain_level_min__lte=pain_val,
                pain_level_max__gte=pain_val,
            )
        except ValueError:
            pass

    diagnoses = Diagnosis.objects.all()
    phases = Exercise.PHASE_CHOICES

    return render(request, 'exercises/list.html', {
        'exercises': exercises,
        'diagnoses': diagnoses,
        'phases': phases,
        'selected_diagnosis': diagnosis_slug or '',
        'selected_phase': phase or '',
        'selected_pain': pain or '5',
    })


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise.objects.select_related('diagnosis'), pk=pk)
    related = Exercise.objects.filter(
        diagnosis=exercise.diagnosis,
        phase=exercise.phase,
    ).exclude(pk=pk)[:4]
    return render(request, 'exercises/detail.html', {
        'exercise': exercise,
        'related': related,
    })
