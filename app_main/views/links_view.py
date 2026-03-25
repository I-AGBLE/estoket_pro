from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

   
from ..forms import LinksForm

@login_required
def links_index(request):
    # Fetch all links for this user
    links = request.user.links.all()

    if request.method == 'POST':
        link_form = LinksForm(request.POST)
        if link_form.is_valid():
            link = link_form.save(commit=False)
            link.user = request.user
            link.save()
            # Redirect to the same page to show fresh form and updated list
            return redirect('app_main:links_index')
    else:
        link_form = LinksForm()

    return render(request, 'links/index.html', {
        'links_form': link_form,
        'links': links
    })