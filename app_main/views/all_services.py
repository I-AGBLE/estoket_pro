from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from ..models.service import Service


def all_services(request):
    services_list = Service.objects.select_related('user').order_by('-created_at')

    paginator = Paginator(services_list, 6)
    page_number = request.GET.get('page', 1)
    services = paginator.get_page(page_number)

    # AJAX response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = []
        for service in services:
            data.append({
                'id': service.id,
                'title': service.service_title,
                'category': service.category,
                'image': service.service_image.url if service.service_image else '',
                'description': service.service_description[:150],
                'user_name': f"{service.user.first_name} {service.user.last_name}",
            })

        return JsonResponse({
            'data': data,
            'has_next': services.has_next()
        })

    return render(request, 'service/all_services.html', {
        'services': services
    })