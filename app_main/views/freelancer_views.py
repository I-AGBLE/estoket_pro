from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms import FreelancerForm


@login_required
def freelancer_index(request):
    if request.method == 'POST':
        freelancer_form = FreelancerForm(request.POST, request.FILES)
        if freelancer_form.is_valid():
            freelancer = freelancer_form.save(commit=False)
            freelancer.user = request.user
            freelancer.save()
            return redirect('app_main:links_index')
    else:
        freelancer_form = FreelancerForm()
    return render(request, 'freelancer/index.html', {'freelancer_form': freelancer_form})




@login_required
def freelancer_dashboard(request):
    return render(request, 'freelancer/freelancer_dashboard.html')

