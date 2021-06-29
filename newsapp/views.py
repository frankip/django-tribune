from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def about(request):

    return render(request, 'about.html')

def about_name(request, name):
    ctx = {
        "name" : name
        }
    print('name',name )
    return render(request, 'about1.html', ctx)