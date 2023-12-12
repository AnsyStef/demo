from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')
def home_eng(request):
    return render(request, 'home_page_eng.html')
