from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import ServiceForm
from ..models import Company  # if needed



# views.py
@login_required
def service_index(request):
    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES)

        if service_form.is_valid():
            service = service_form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect('app_main:service_detail', service_id=service.id)
    else:
        service_form = ServiceForm()

    return render(request, 'service/index.html', {'service_form': service_form})
    
    

def service_detail(request, service_id):
    
    return render(request, 'service/service_detail.html')