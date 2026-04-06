from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import LinksForm
from ..models import Links  # make sure Link model is imported


@login_required
def links_index(request):
    links = request.user.links.all()  # fetch all links for this user

    # Check if we are editing a link
    link_id = request.GET.get('edit')
    link_instance = None
    if link_id:
        link_instance = get_object_or_404(links, id=link_id)

    # Initialize form
    form = LinksForm(instance=link_instance)

    if request.method == 'POST':
        # ------------------- Complete Profile button -------------------
        if 'complete_profile' in request.POST:
            if request.user.user_type == 'company':
                return redirect('app_main:company_dashboard')
            elif request.user.user_type == 'freelancer':
                return redirect('app_main:freelancer_dashboard')
            else:
                return redirect('app_users:index')

        # ------------------- Handle Add/Edit -------------------
        link_id = request.POST.get('link_id')
        if link_id:
            # Delete old link before replacing
            old_link = get_object_or_404(links, id=link_id)
            old_link.delete()

        form = LinksForm(request.POST)
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.user = request.user

            # Prevent duplicate links
            if request.user.links.filter(platform=new_link.platform, address=new_link.address).exists():
                form.add_error(None, "This link already exists.")
            else:
                new_link.save()
                messages.success(request, "Link saved successfully!")
                return redirect('app_main:links_index')

    return render(request, 'links/index.html', {
        'links_form': form,
        'links': links,
        'editing': link_id
    })


# ------------------- Delete Link View -------------------
@login_required
def delete_link(request, link_id):
    link = get_object_or_404(Link, id=link_id, user=request.user)
    link.delete()
    messages.success(request, "Link deleted!")
    return redirect('app_main:links_index')