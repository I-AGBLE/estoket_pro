from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from ..forms import CompanyForm
from ..models import Company




@login_required
def company_index(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.user = request.user  # assign FK automatically
            company.save()
            return redirect('app_main:links_index')  # or company_detail view
    else:
        company_form = CompanyForm()

    return render(request, 'company/index.html', {'company_form': company_form})





@login_required
def company_dashboard(request):
    company = None

    # Get the company linked to this user
    try:
        company = request.user.companies.first()  # since you used ForeignKey
    except:
        company = None

    # Get user links
    links = request.user.links.all()

    return render(request, 'company/company_dashboard.html', {
        'company': company,
        'links': links
    })
    
    
    



def custom_website(request, slug):
    # Get company using slug
    company = get_object_or_404(Company, slug=slug)

    # Get the user linked to the company
    user = company.user

    # Get links belonging to that user
    links = user.links.all()

    return render(request, 'company/custom_website.html', {
        'company': company,
        'user': user,
        'links': links
    })


#from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

#@login_required
#def company_index(request):
    #return render(request, 'company/index.html')

