from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import QueryForm
from core.models import Player

def index(request):
    context = {}
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['query'].split()
            player = Player.objects.get(first_name=name[0], last_name=name[1])

        #DO QUERY STUFF HERE

        context = { 'form': form, 'player': player } #add return data here
    else:
        form = QueryForm()
        context = { 'form': form, }

    return render(request, 'core/index.html', context)
