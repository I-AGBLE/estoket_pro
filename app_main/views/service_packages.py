from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models.service import Service
from ..models import ServicePackage
from ..forms import ServicePackageForm





@login_required
def service_packages(request, service_id):
    service = get_object_or_404(Service, id=service_id, user=request.user)

    package_id = request.GET.get('edit')  # 👈 check if editing
    package_instance = None

    if package_id:
        package_instance = get_object_or_404(ServicePackage, id=package_id, service=service)

    # 👇 use instance if editing
    service_package_form = ServicePackageForm(instance=package_instance)

    if request.method == 'POST':
        package_id = request.POST.get('package_id')
        package_instance = None

        if package_id:
            package_instance = get_object_or_404(ServicePackage, id=package_id, service=service)

        service_package_form = ServicePackageForm(request.POST, instance=package_instance)

        if service_package_form.is_valid():
            package = service_package_form.save(commit=False)
            package.service = service

            try:
                package.save()

                if package_instance:
                    messages.success(request, "Package updated!")
                else:
                    messages.success(request, "Package added!")

                if request.POST.get('action') == 'next':
                    return redirect('app_main:service_expertise', service_id=service.id)
                else:
                    return redirect('app_main:service_packages', service_id=service.id)

            except:
                service_package_form.add_error('package_type', 'This package type already exists.')

    packages = service.packages.all()

    return render(request, 'service/service_packages.html', {
        'service': service,
        'service_package_form': service_package_form,
        'packages': packages,
        'editing': package_instance  # 👈 pass to template
    })
    




@login_required
def delete_service_package(request, package_id):
    package = get_object_or_404(ServicePackage, id=package_id, service__user=request.user)
    service_id = package.service.id

    package.delete()
    messages.success(request, "Package deleted!")

    return redirect('app_main:service_packages', service_id=service_id)