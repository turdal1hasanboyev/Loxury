from django.shortcuts import render

def home(request):
    ctx = {

    }

    return render(request=request, template_name='index.html', context=ctx)