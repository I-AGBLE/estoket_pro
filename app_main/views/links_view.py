from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

   
from ..forms import LinksForm

@login_required
def links_index(request):
    links = request.user.links.all()

    if request.method == 'POST':

        # 👇 If "Complete Profile" button was clicked
        if 'complete_profile' in request.POST:
            if request.user.user_type == 'company':
                return redirect('app_main:company_dashboard')
            elif request.user.user_type == 'freelancer':
                return redirect('app_main:freelancer_dashboard')
            else:
                return redirect('app_users:index')

        # 👇 Otherwise, handle normal form submission
        link_form = LinksForm(request.POST)
        if link_form.is_valid():
            link = link_form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('app_main:links_index')

    else:
        link_form = LinksForm()

    return render(request, 'links/index.html', {
        'links_form': link_form,
        'links': links
    })