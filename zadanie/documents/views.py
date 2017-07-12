from django.shortcuts import render
from .forms import StringForm
from .models import String

def uploadText(request):
    form = StringForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'documents.html', locals())

def getText(request):
    string1 = String.objects.filter()
    return render(request, 'get.html', locals())