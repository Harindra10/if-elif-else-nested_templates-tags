from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':400,'b':600,'c':300}
    return render(request,'condition.html',d)


def nested(request):
    d={'a':400,'b':600,'c':300}
    return render(request,'nested.html',d)