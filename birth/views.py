from django.shortcuts import render, redirect
from .models import Father, Mother, Child
from .forms import FatherForm, MotherForm, ChildForm
from django.http import  HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    children = Child.objects.all().order_by('first_name')
    return render(request, 'birth/home.html', {
        'children': children,
    })
    

@login_required
def add_father(request):
    submitted = False
    if request.method == "POST":
        form = FatherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_father?submitted=True')
    else:
        form = FatherForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'birth/add_father.html', {
        'form': form,
        'submitted': submitted,
    })

@login_required
def add_mother(request):
    submitted = False
    if request.method == "POST":
        form = MotherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_mother?submitted=True')
    else:
        form = MotherForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'birth/add_mother.html', {
        'form': form,
        'submitted': submitted,
    })

@login_required
def add_child(request,):
    submitted = False
    if request.method == "POST":
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_child?submitted=True')
    else:
        form = ChildForm
        if 'submitted' in request.GET:
            submitted=True
            
    """ def form_valid(self, form):
        form.instance.author = self.user
        return super().form_valid(form) """
        
    return render(request, 'birth/add_child.html', {
        'form': form,
        'submitted': submitted,
    })

@login_required
def children_list(request):
    children = Child.objects.all().order_by('first_name')
    return render(request, 'birth/children_list.html', {
        'children': children,
    })
    
@login_required
def show_child(request, child_id):
    child = Child.objects.get(pk=child_id)
    return render(request, 'birth/show_child.html', {
        'child': child,
    })
    
@login_required
def update_child(request, child_id):
    child = Child.objects.get(pk=child_id)
    form = ChildForm(request.POST or None, instance=child)
    if form.is_valid():
        form.save()
        return redirect('children-list')
    return render(request, 'birth/update_child.html', {
        'student': child,
        'form': form,
    }) 

@login_required   
def search_child(request):
    if request.method == "POST":
        searched = request.POST['searched']
        children = Child.objects.filter(first_name__contains=searched)
        return render(request, 'birth/search_child.html', {
            'searched': searched,
            'children': children
        })
    else:
        return render(request, 'birth/search_child.html', {})