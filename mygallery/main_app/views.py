from django.shortcuts import render, redirect
from .models import Sculpture

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

@login_required
def sculpture_index(request):
    sculptures = Sculpture.objects.filter(user=request.user)
    return render(request, 'sculptures/index.html', {'sculptures': sculptures})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sculpture-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def sculpture_index(request):
    sculptures = Sculpture.objects.filter(user=request.user) 
    return render(request, 'sculptures/index.html', {'sculptures': sculptures})

@login_required
def sculpture_detail(request, sculpture_id):
    from .models import Sculpture
    sculpture = Sculpture.objects.get(id=sculpture_id)
    return render(request, 'sculptures/detail.html', {'sculpture': sculpture})

class SculptureCreate(LoginRequiredMixin, CreateView):
    model = Sculpture
    fields = ['title', 'artist', 'year_created', 'description', 'file']
    success_url = '/sculptures/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SculptureUpdate(LoginRequiredMixin, UpdateView):
    model = Sculpture
    fields = ['title', 'artist', 'description', 'year_created', 'file']

class SculptureDelete(LoginRequiredMixin, DeleteView):
    model = Sculpture
    success_url = '/sculptures/'


