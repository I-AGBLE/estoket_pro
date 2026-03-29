from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models.service import Service
from ..models.faqs import FAQ
from ..forms import FAQForm

@login_required
def service_faqs(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    form = FAQForm()

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.service = service
            faq.save()
            messages.success(request, f"FAQ added!")

            # Determine which button was clicked
            if request.POST.get('action') == 'next':
                return redirect('app_main:service_detail', service_id=service.id)  # Go to service details page
            else:
                return redirect('app_main:service_faqs', service_id=service.id)  # Stay to add more

    faqs = service.faqs.all()
    return render(request, 'service/service_faqs.html', {
        'service': service,
        'form': form,
        'faqs': faqs
    })