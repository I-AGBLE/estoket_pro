from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from app_main.models.service import Service

from ..forms import ServicePackageForm


from ..models import ServicePackage



@login_required
def service_packages(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service_package_form = ServicePackageForm()

    if request.method == 'POST':
        service_package_form = ServicePackageForm(request.POST)
        if service_package_form.is_valid():
            package = service_package_form.save(commit=False)
            package.service = service
            try:
                package.save()
                messages.success(request, f"{package.package_type.title()} package added!")
                return redirect('app_main:service_packages', service_id=service.id)
            except:
                service_package_form.add_error('package_type', 'This package type already exists for this service.')

    packages = service.packages.all()
    return render(request, 'service/service_packages.html', {
        'service': service,
        'service_package_form': service_package_form,
        'packages': packages
    })