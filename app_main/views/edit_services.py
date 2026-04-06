from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models.service import Service
from ..forms import ServiceForm


@login_required
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, user=request.user)

    # Get existing categories for datalist
    categories = Service.objects.values_list('category', flat=True).distinct()

    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES, instance=service)

        if service_form.is_valid():
            service = service_form.save(commit=False)
            service.category = service.category.strip().title()
            service.save()

            messages.success(request, "Service updated successfully!")

            # 👉 Continue flow to packages
            return redirect('app_main:service_packages', service_id=service.id)
    else:
        service_form = ServiceForm(instance=service)

    return render(request, 'service/edit_service.html', {
        'service_form': service_form,
        'service': service,
        'categories': categories
    })