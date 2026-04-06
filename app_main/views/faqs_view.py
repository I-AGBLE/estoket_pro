from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models.service import Service
from ..models.faqs import FAQ
from ..forms import FAQForm


    
@login_required
def service_faqs(request, service_id):
    service = get_object_or_404(Service, id=service_id, user=request.user)

    faq_id = request.GET.get('edit')
    faq_instance = None

    if faq_id:
        faq_instance = get_object_or_404(service.faqs.model, id=faq_id, service=service)

    form = FAQForm(instance=faq_instance)

    if request.method == 'POST':
        faq_id = request.POST.get('faq_id')
        if faq_id:
            old_faq = get_object_or_404(service.faqs.model, id=faq_id, service=service)
            old_faq.delete()  # replace old

        form = FAQForm(request.POST)
        if form.is_valid():
            new_faq = form.save(commit=False)
            new_faq.service = service
            new_faq.save()

            if request.POST.get('action') == 'next':
                return redirect('app_main:service_detail', service_id=service.id)
            else:
                return redirect('app_main:service_faqs', service_id=service.id)

    faqs = service.faqs.all()

    return render(request, 'service/service_faqs.html', {
        'service': service,
        'form': form,
        'faqs': faqs,
        'editing': faq_id
    })


# Delete FAQ
@login_required
def delete_service_faq(request, faq_id):
    faq = get_object_or_404(Service.faqs.model, id=faq_id, service__user=request.user)
    service_id = faq.service.id
    faq.delete()
    messages.success(request, "FAQ deleted!")
    return redirect('app_main:service_faqs', service_id=service_id)