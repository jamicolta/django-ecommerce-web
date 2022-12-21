from django.urls import path
from .views import (
    render_post,
    registrarComentario,
    registrarCurso,
    eliminarCurso,
    edicionCurso,
    editarCurso,
    contact,
    form_detail,
)

app_name = "form"

urlpatterns = [
    path("", render_post, name="form"),
    path("<int:form_id>", form_detail, name="form_detail"),
    path("registrarComentario/", registrarComentario),
    path("registrarCurso/", registrarCurso),
    path("edicionCurso/<id>", edicionCurso),
    path("editarCurso/", editarCurso),
    path("eliminarCurso/<id>", eliminarCurso),
    path("contact/", contact, name="contact"),
]
