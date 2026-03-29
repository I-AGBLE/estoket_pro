from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..forms import ServiceForm
from ..models import Company, Service



# views.py
@login_required
def service_index(request):
    # Get existing categories (for datalist suggestions)
    categories = Service.objects.values_list('category', flat=True).distinct()

    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES)

        if service_form.is_valid():
            service = service_form.save(commit=False)
            service.user = request.user

            # Optional: normalize category (avoid duplicates like "design" vs "Design")
            service.category = service.category.strip().title()

            service.save()
            return redirect('app_main:service_packages', service_id=service.id)
    else:
        service_form = ServiceForm()

    return render(request, 'service/index.html', {
        'service_form': service_form,
        'categories': categories  # 👈 pass to template
    })
    
    
    
    

def service_detail(request, service_id):
    # Fetch the service or return 404 if it doesn't exist
    service = get_object_or_404(Service, id=service_id)

    # Pass the service to the template
    return render(request, 'service/service_detail.html', {'service': service})







