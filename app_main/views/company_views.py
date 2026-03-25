from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms import CompanyForm

@login_required
def company_index(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.user = request.user  # assign FK automatically
            company.save()
            return redirect('app_main:company_links')  # or company_detail view
    else:
        company_form = CompanyForm()

    return render(request, 'company/index.html', {'company_form': company_form})






def company_links(request):
    return render(request, 'company/company_links.html')


#from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

#@login_required
#def company_index(request):
    #return render(request, 'company/index.html')

