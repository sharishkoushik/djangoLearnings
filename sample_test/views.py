from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from .models import NotesDB
from .forms import NotesDBForm
# Create your views here.


def home(request):
	# all_items = List.objects.all
    all_items = NotesDB.objects.order_by('date')
    cntxt = {'all_items' : all_items}
    return render(request, 'home.html', cntxt)

# def formpage(request):
# 	# context = {'firstname' : 'Harish', 'lastname' : 'Koushik'}
# 	return render(request, 'formpage.html', {})

def formpage(request):

    form = NotesDBForm()

    if request.method == "POST":
        form = NotesDBForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            all_items = NotesDB.objects.order_by('date')
            cntxt = {'all_items' : all_items}
            print("Printing from formpage", cntxt)
            return HttpResponseRedirect("/")
        else:
            print("INVALID FORM")
    return render(request, "formpage.html",{'form': form})

    # return render(request,'formpage.html',{'form':form})
