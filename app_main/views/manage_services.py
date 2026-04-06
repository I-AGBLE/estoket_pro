from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models.service import Service


@login_required
def manage_services(request):
    services = Service.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'service/manage_services.html', {
        'services': services
    })