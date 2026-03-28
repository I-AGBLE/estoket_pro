from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import LinksForm

@login_required
def links_index(request):
    # Fetch all links belonging to this user
    links = request.user.links.all()

    if request.method == 'POST':
        # ------------------- Complete Profile button -------------------
        if 'complete_profile' in request.POST:
            if request.user.user_type == 'company':
                return redirect('app_main:company_dashboard')
            elif request.user.user_type == 'freelancer':
                return redirect('app_main:freelancer_dashboard')
            else:
                return redirect('app_users:index')

        # ------------------- Add new link -------------------
        link_form = LinksForm(request.POST)
        if link_form.is_valid():
            new_link = link_form.save(commit=False)
            new_link.user = request.user

            # Prevent duplicate links for the same user
            if not request.user.links.filter(
                platform=new_link.platform,
                address=new_link.address
            ).exists():
                new_link.save()

            # Refresh the page (new empty form and updated list)
            return redirect('app_main:links_index')

    else:
        link_form = LinksForm()  # empty form

    return render(request, 'links/index.html', {
        'links_form': link_form,
        'links': links
    })