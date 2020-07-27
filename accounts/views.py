from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, ChangeDefaultTimesForm
import json


# Create your views here.
def create_account_view(request, *args, **kwargs):
    # Only process if a post request is sent
    if request.method == 'POST':

        create_account_form = SignUpForm(request.POST)

        # If the form has correct information it can be stored
        if create_account_form.is_valid():
            create_account_form.save()
            username = create_account_form.cleaned_data.get('username')
            password = create_account_form.cleaned_data.get('password1')
            email = create_account_form.cleaned_data.get('email')

            # Login to the account instantly
            user = authenticate(username=username, password=password)
            login(request, user)

            # Return back to the main screen
            return redirect('index')
    else:
        create_account_form = SignUpForm()

    my_context = {
        'form': create_account_form,
    }

    return render(request, 'accounts/create_account.html', my_context)


def profile_view(request):
    user = User.objects.get(username=request.user.username)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)


def change_default_times_view(request):
    user_profile = User.objects.get(username=request.user.username).userprofile
    form = ChangeDefaultTimesForm(request.POST or None, instance=user_profile)

    if form.is_valid():
        form.save()
        return redirect('profile')

    context = {
        'UserProfile': user_profile,
        'form': form
    }

    return render(request, 'accounts/change_default_times.html', context)


def upgrade(request):
    plant_number = int(request.GET["plant_id"])
    upgrade_cost = int(request.GET["plant_cost"])

    if request.user.is_authenticated and request.user.userprofile.score >= upgrade_cost:
        request.user.userprofile.score = request.user.userprofile.score - upgrade_cost

        if plant_number == 1:
            plant_stage = request.user.userprofile.plant1_stage
            if plant_stage < 7:
                new_stage = plant_stage + 1
                request.user.userprofile.plant1_stage = new_stage
            else:
                new_stage = 1
                request.user.userprofile.plant1_stage = new_stage
                request.user.userprofile.award_count = request.user.userprofile.award_count + 1

        elif plant_number == 2:
            plant_stage = request.user.userprofile.plant2_stage
            if plant_stage < 7:
                new_stage = plant_stage + 1
                request.user.userprofile.plant2_stage = new_stage
            else:
                new_stage = 1
                request.user.userprofile.plant2_stage = new_stage
                request.user.userprofile.award_count = request.user.userprofile.award_count + 1

        elif plant_number == 3:
            plant_stage = request.user.userprofile.plant3_stage
            if plant_stage < 7:
                new_stage = plant_stage + 1
                request.user.userprofile.plant3_stage = new_stage
            else:
                new_stage = 1
                request.user.userprofile.plant3_stage = new_stage
                request.user.userprofile.award_count = request.user.userprofile.award_count + 1

        request.user.userprofile.save()

        data = {'score': request.user.userprofile.score, 'new_stage': new_stage}
        json_data = json.dumps(data)

        return HttpResponse(json_data)
    else:
        return HttpResponse('FALSE')
