from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from django.template import loader
from .models import GeeksModel
from .file_forms import GeeksForm

# Create your views here.
def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request,"create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = GeeksModel.objects.all()
    return render(request, "list_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id = id)
    form = GeeksForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"]=form
    return render(request, 'update_view.html',context)

def delete_view(request, id):
    context ={}
    obj = get_object_or_404(GeeksModel, id = id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"delete_view.html", context)