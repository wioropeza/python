from django.http import HttpResponse
from django.template import loader
from MiFamilia.models import Familiar


def agregadofamiliar(self):
    familiar1 = Familiar(parentesco="Madre", nombre="Adriana", apellido="Caceres", edad=55, fechaDeNacimiento="1967-10-14")
    familiar2 = Familiar(parentesco="Hermano", nombre="Yohan", apellido="Caceres", edad=37, fechaDeNacimiento="1985-04-04")
    familiar3 = Familiar(parentesco="Hermano", nombre="Omar", apellido="Oropeza", edad=35, fechaDeNacimiento="1990-09-09")
    familiar4 = Familiar(parentesco="Hermana", nombre="Alondra", apellido="Oropeza", edad=26, fechaDeNacimiento="1995-06-03")
    familiar5 = Familiar(parentesco="Pareja", nombre="Federico", apellido="Pezzutti", edad=30, fechaDeNacimiento="1984-05-03")
    
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    familiar5.save()
    
    documento = f'Parentesco: {familiar1.parentesco} - Nombre: {familiar1.nombre} - Apellido {familiar1.apellido} - Edad: {familiar1.edad} - Fecha de nacimiento: {familiar1.fechaDeNacimiento}<br>Parentesco: {familiar2.parentesco} - Nombre: {familiar2.nombre} - Apellido {familiar2.apellido} - Edad: {familiar2.edad} - Fecha de nacimiento: {familiar2.fechaDeNacimiento}<br>Parentesco: {familiar3.parentesco} - Nombre: {familiar3.nombre} - Apellido {familiar3.apellido} - Edad: {familiar3.edad} - Fecha de nacimiento: {familiar3.fechaDeNacimiento}<br>Parentesco: {familiar4.parentesco} - Nombre: {familiar4.nombre} - Apellido {familiar4.apellido} - Edad: {familiar4.edad} - Fecha de nacimiento: {familiar4.fechaDeNacimiento}<br>Parentesco: {familiar5.parentesco} - Nombre: {familiar5.nombre} - Apellido {familiar5.apellido} - Edad: {familiar5.edad} - Fecha de nacimiento: {familiar5.fechaDeNacimiento}'
    
    return HttpResponse(documento)


