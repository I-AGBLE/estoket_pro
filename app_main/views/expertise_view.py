from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models.service import Service
from ..models.expertise import Expertise
from ..forms import ExpertiseForm



@login_required
def service_expertise(request, service_id):
    service = get_object_or_404(Service, id=service_id, user=request.user)

    expertise_id = request.GET.get('edit')
    expertise_instance = None

    if expertise_id:
        expertise_instance = get_object_or_404(service.expertises.model, id=expertise_id, service=service)

    form = ExpertiseForm(instance=expertise_instance)

    if request.method == 'POST':
        expertise_id = request.POST.get('expertise_id')
        if expertise_id:
            old_expertise = get_object_or_404(service.expertises.model, id=expertise_id, service=service)
            old_expertise.delete()  # replace old

        form = ExpertiseForm(request.POST)
        if form.is_valid():
            new_expertise = form.save(commit=False)
            new_expertise.service = service
            new_expertise.save()

            if request.POST.get('action') == 'next':
                return redirect('app_main:service_faqs', service_id=service.id)
            else:
                return redirect('app_main:service_expertise', service_id=service.id)

    expertises = service.expertises.all()

    return render(request, 'service/service_expertise.html', {
        'service': service,
        'form': form,
        'expertises': expertises,
        'editing': expertise_id
    })
    

# Delete Expertise
@login_required
def delete_service_expertise(request, expertise_id):
    expertise = get_object_or_404(Service.expertises.model, id=expertise_id, service__user=request.user)
    service_id = expertise.service.id
    expertise.delete()
    messages.success(request, "Expertise deleted!")
    return redirect('app_main:service_expertise', service_id=service_id)
