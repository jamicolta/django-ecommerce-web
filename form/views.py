from django.shortcuts import render, redirect, get_object_or_404
from .models import Form, Legend
from main.models import Project
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.
@login_required(login_url="/")
def render_post(request):
    forms = Form.objects.all()
    return render(request, "form.html", {"forms": forms})


@login_required(login_url="/")
def registrarComentario(request):
    comment = request.POST["comment"]
    user = request.POST["user"]
    legends = Legend.objects.create(comment=comment, user=user)
    return redirect("/")


@login_required(login_url="/")
def registrarCurso(request):
    id = request.POST["id"]
    rol = request.POST["rol"]
    title = request.POST["title"]
    description = request.POST["description"]
    date = request.POST["date"]
    image = request.FILES["image"]
    form = Form.objects.create(
        id=id, rol=rol, title=title, description=description, date=date, image=image
    )
    return redirect("/")


@login_required(login_url="/")
def edicionCurso(request, id):
    form = Form.objects.get(id=id)
    return render(request, "edicionCurso.html", {"form": form})


def editarCurso(request):
    title = request.POST["title"]
    description = request.POST["description"]
    date = request.POST["date"]
    id = request.POST["id"]
    form = Form.objects.get(id=id)
    form.title = title
    form.description = description
    form.date = date
    form.id = id
    form.save()
    return redirect("/")


@login_required(login_url="/")
def eliminarCurso(request, id):
    form = Form.objects.get(id=id)
    form.delete()
    return redirect("/")


@login_required(login_url="/")
def contact(request):
    if request.method == "POST":
        newsletter = request.POST["newsletter"]
        template = render_to_string("email_template.html", {"newsletter": newsletter})
        email = EmailMessage(
            newsletter,
            template,
            settings.EMAIL_HOST_USER,
            ["julian.micolta26@gmail.com"],
        )
        email.fail_silently = False
        email.send()
        messages.success(request, "Se ha enviado el newsletter correctamente!")
        return redirect("/")


def form_detail(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    projects = Project.objects.all()
    legends = Legend.objects.all()
    return render(
        request,
        "form_detail.html",
        {"form": form, "projects": projects, "legends": legends},
    )
