from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models.service import Service
from ..models.expertise import Expertise
from ..forms import ExpertiseForm

@login_required
def service_expertise(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    form = ExpertiseForm()

    if request.method == 'POST':
        form = ExpertiseForm(request.POST)
        if form.is_valid():
            expertise = form.save(commit=False)
            expertise.service = service
            expertise.save()
            messages.success(request, f"{expertise.expertise_title} added!")

            # Check which button was clicked
            if request.POST.get('action') == 'next':
                # Redirect to the FAQs page for this service
                return redirect('app_main:service_faqs', service_id=service.id)
            else:
                # Stay on the expertise page to add more
                return redirect('app_main:service_expertise', service_id=service.id)

    expertises = service.expertises.all()
    return render(request, 'service/service_expertise.html', {
        'service': service,
        'form': form,
        'expertises': expertises
    })