from django.shortcuts import render

# Create your views here.
def company_index(request):
    return render(request, 'company/index.html')


def freelancer_index(request):
    return render(request, 'freelancer/index.html')

