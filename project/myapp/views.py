from django.shortcuts import render
from .forms import detailsForm
from .models import myform


def form(request):
    data = myform.objects.all()
    if request.method == 'POST':
        form = detailsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = detailsForm()
    return render(request, 'myapp/form.html', {'form': form, 'data': data})
def table(request):
    data = myform.objects.all()
    return render(request,'myapp/table.html',{'data':data}) 