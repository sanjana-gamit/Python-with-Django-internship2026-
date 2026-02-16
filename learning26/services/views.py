from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm


# LIST
def service_list(request):
    services = Service.objects.all()
    return render(request, "services/service_list.html", {"services": services})


# CREATE
def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("services:service_list")
    else:
        form = ServiceForm()
    return render(request, "services/service_form.html", {"form": form})


# UPDATE
def service_update(request, id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("services:service_list")
    else:
        form = ServiceForm(instance=service)
    return render(request, "services/service_form.html", {"form": form})


# DELETE
def service_delete(request, id):
    Service.objects.filter(id=id).delete()
    return redirect("services:service_list")
