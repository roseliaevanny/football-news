from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406410235',
        'name': 'Roselia Evanny Sucipto',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)