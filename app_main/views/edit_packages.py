from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models.service import Service
from ..forms import ServicePackageForm



@login_required
def edit_service_packages(request, service_id):
    service = get_object_or_404(Service, id=service_id, user=request.user)
    form = ServicePackageForm()

    if request.method == 'POST':
        form = ServicePackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.service = service
            try:
                package.save()
                messages.success(request, "Package saved!")

                if request.POST.get('action') == 'next':
                    return redirect('app_main:edit_service_expertise', service_id=service.id)
                else:
                    return redirect('app_main:edit_service_packages', service_id=service.id)

            except:
                form.add_error('package_type', 'Package type already exists.')

    packages = service.packages.all()

    return render(request, 'service/edit_packages.html', {
        'service': service,
        'form': form,
        'packages': packages
    })