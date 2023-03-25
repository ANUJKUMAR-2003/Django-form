from django.shortcuts import render
from .forms import detailsForm
from .models import myform

from django.views.decorators.cache import cache_control

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def form(request):
    data = myform.objects.all()
    if request.method == 'POST':
        form = detailsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = detailsForm()
    return render(request, 'myapp/form.html', {'form': form, 'data': data})

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def table(request):
    data = myform.objects.all()
    return render(request,'myapp/table.html',{'data':data}) 