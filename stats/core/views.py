from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import QueryForm
from core.models import Player
from core.parser import parse_input

def index(request):
    context = {}
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            stuff = parse_input(cd['query'])
        #DO QUERY STUFF HERE

        context = { 'form': form, 'data': stuff } #add return data here
    else:
        form = QueryForm()
        context = { 'form': form, }

    return render(request, 'core/index.html', context)
