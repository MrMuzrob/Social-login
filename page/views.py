from django.shortcuts import render


# Create your views here.

def FirstPage(request):
    return render(request, 'dashboard/first_page.html')