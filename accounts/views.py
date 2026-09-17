from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, QuestionnaireForm
from .models import PatientProfile


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            PatientProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created! Please complete your questionnaire.')
            return redirect('accounts:questionnaire')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'pages:home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('pages:home')


@login_required
def questionnaire_view(request):
    profile, _ = PatientProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.questionnaire_completed = True
            profile.save()
            messages.success(request, 'Questionnaire saved! Your experience is now personalized.')
            return redirect('pages:home')
    else:
        form = QuestionnaireForm(instance=profile)
    return render(request, 'accounts/questionnaire.html', {'form': form})


@login_required
def profile_view(request):
    profile, _ = PatientProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})
