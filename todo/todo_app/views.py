from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import todoForm
from django. views.generic import ListView
from django. views . generic import DetailView
from django.views . generic .edit import UpdateView,DeleteView

# Create your views here.

class listing(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'TASK'
class details(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'variable'

def demo(request):
    var = task.objects.all()
    if request.method == 'POST':
        NAME = request.POST.get('task', ' ')
        PRIORITY = request.POST.get('priority', ' ')
        DATE = request.POST.get('date', ' ')

        var1 = task(name=NAME, priority= PRIORITY, date = DATE)
        var1.save()
    return render(request,"home.html", {'TASK': var})

class deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('classview')

def delete(request, taskid):
    var2 = task.objects.get(id=taskid)
    if request.method == 'POST':
        var2.delete()
        return redirect('/')
    return render(request, "delete.html")

class updateview(UpdateView):
    model = task
    template_name = 'update1.html'
    context_object_name = 'variable1'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.id})

def update(request, taskid):
    var3 = task.objects.get(id=taskid)
    var4 = todoForm(request.POST or None, instance= var3)
    if var4.is_valid():
        var4.save()
        return redirect('/')
    return render(request, 'update.html', {'form': var4, 'TASK': var3})

