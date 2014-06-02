from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import QueryForm

def index(request):
    context = {}
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['query']

        #DO QUERY STUFF HERE

        context = { 'form': form, } #add return data here
    else:
        form = QueryForm()
        context = { 'form': form, }

    return render(request, 'core/index.html', context)
