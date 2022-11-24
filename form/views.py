from django.shortcuts import render, redirect
from .models import Form

# Create your views here.
def render_post(request):
    forms = Form.objects.all()
    return render(request, 'form.html', {'forms': forms})

def registrarCurso(request):
    id = request.POST['id']
    rol = request.POST['rol']
    title = request.POST['title']
    description = request.POST['description']
    date = request.POST['date']
    image = request.POST['image']
    form = Form.objects.create(id=id, rol=rol, title=title, description=description, date=date, image=image)
    return redirect('/')

def edicionCurso(request, id):
    form = Form.objects.get(id = id)
    return render(request, 'edicionCurso.html', {'form': form})

def editarCurso(request):
    title = request.POST['title']
    id = request.POST['id']
    form = Form.objects.get(id = id)
    form.title = title
    form.id = id
    form.save()
    return redirect('/')

def eliminarCurso(request, id):
    form = Form.objects.get(id = id)
    form.delete()
    return redirect('/')