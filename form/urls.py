from django.urls import path
from .views import render_post, registrarCurso, eliminarCurso, edicionCurso, editarCurso, contact

app_name = 'form'

urlpatterns = [
    path('', render_post, name='form'),
    path('registrarCurso/', registrarCurso),
    path('edicionCurso/<id>', edicionCurso),
    path('editarCurso/', editarCurso),
    path('eliminarCurso/<id>', eliminarCurso),
    path('contact/', contact, name='contact')
]