from django.shortcuts import render, redirect
from .forms import CategoryForm

def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('category_form')

    form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})