from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm, SearchForm
from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponse


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('clients:client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_edit.html', {'form': form})


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:client_list')
        elif 'cancel' in request.POST:
            return redirect('clients:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_edit.html', {'form': form, 'client': client})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        if 'confirm' in request.POST:
            client.delete()
            return redirect('clients:client_list')
        elif 'cancel' in request.POST:
            return redirect('clients:client_list')

    return render(request, 'clients/client_delete.html', {'client': client})


def client_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            clients = Client.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(middle_name__icontains=query) |
                Q(date_of_birth__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(address__icontains=query) |
                Q(email__icontains=query)
            )
            return render(request, 'clients/search_results.html', {'clients': clients})
    else:
        form = SearchForm()
    return render(request, 'clients/client_search.html', {'form': form})

def client_photo(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if not client.photo:
        return HttpResponseNotFound()
    return HttpResponse(client.photo, content_type='image/jpeg')
