#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

#        ENGAGEMENT CALCULADORA v.2.3 by FRANCO PEREZ (github> devlang)

#       check - agregar comprobacion de modules

# 31 de ago 2020: cambiar codigo para usar una clase que contenga los datos a usar
# y llamar desde una funcion a esa clase

# v.2.2.3.9
# v.2.3 implementacion de clases (implementado en institucion,
# probar implementar en la funcion de engagement

# 3 de sep 2020:
# v.2.3.0.1 correcciones menores

# VER si puedo recortar codigo en la funcion de ingreso de datos

import pkg_resources

#comprobacion de modulos BETA
for package in ['colorama', 'datetime', 'termcolor', 'ansimarkup']:
    try:
        dist = pkg_resources.get_distribution(package)
        #print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('Diagnostico de requisitos')
        print('{} NO se encuentra instalado'.format(package)) 
for package in ['colorama', 'datetime', 'termcolor', 'ansimarkup']:
    try:
        dist = pkg_resources.get_distribution(package)
        #print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('EJECUTAR pip install -r requeriments.txt')
        print ("===========================================")
    pass

try:
    from termcolor import colored
    from colorama import Fore, Style
    from ansimarkup import ansiprint as print
    from datetime import datetime
except:
    pass


ahora = datetime.now()

#GUI TEST SHOULD BE HERE ahre... necesito un module para una buena gui

''' no recuerdo por que las puse
#import math
#import sys
#import os
pero si llegan a necesitarse aqui estan XD '''


#definir un menu
## opciones> 1 AUTOMATICO 2 MANUAL 0 SALIR

''' Habilitar cuando se tenga idea de como ponerlo sin que se loopee '''

#VARIABLES_PLACE
# 31 de ago 2020: usar una clase llamada institucion
'''
por ejemplo:

class Institucion:
    nombre = ""
    lema = ""
'''

''' viejo metodo ''' '''
nombre = "<b>Puerta 18!</b>"
lema = "<b>Donde tu talento es la clave</b>"
edad = "18"
edad_min = "13"
edad_max = "24"
calle = "Zelaya"
numero_calle = " 3118"
'''

class Puerta:
    nombre = "<b>Puerta 18!</b>"
    lema = "<b>Donde tu talento es la clave</b>"
    edad = "18"
    edadmn = "13"
    edadmx = "24"
    calle = "Zelaya"
    numcalle = "3118"

'''
#FUNCION (DEF/VIEJA) PARA USAR VARIABLES_PLACE
def Nombre_Inst():
    #imprime el nombre del lugar
    #imprime el lema del lugar
    print(Fore.MAGENTA + nombre, Fore.BLUE + lema)
    #imprime la direccion
    print(Style.RESET_ALL +calle + numero_calle)
    #condicion etaria para ingresar
    print ("Desde", edad_min, "hasta", edad_max, "anos")
    '''
# FUNCION CON CLASE

def Nombre_Inst():
    #imprime el nombre del lugar
    #imprime el lema del lugar
    print(Fore.MAGENTA + Puerta.nombre, Fore.BLUE + Puerta.lema)
    #imprime la direccion
    print(Style.RESET_ALL +Puerta.calle + Puerta.numcalle)
    #condicion etaria para ingresar
    print ("Desde", Puerta.edadmn, "hasta", Puerta.edadmx, "anos")

def Calc_Engmnt():
    if engagement <= 1:
        print ('Engagement', colored('Bajo', 'red'))
    elif engagement >= 1 and engagement <= 3.5:
        print ('Engagement', colored('Promedio/Bueno', 'blue'))
    elif engagement >= 3.5 and engagement <= 6:
        print ('Engagement', colored('Alto', 'green'))
    elif engagement >= 6:
        print ('Engagement', Fore.MAGENTA + 'Muy Alto' + Style.RESET_ALL)
        #

#depurar

dbg_txt = ("=============== DEBUG =====================")

def Debug():
    print (dbg_txt)
    print ('s', {seguidores}, 'f', {foto1_likes}, {foto2_likes}, {foto3_likes}, 'sum', {total_img_likes}, 'c', {comentarios_total}, 'g', {guardados_total}, 't', {total_img_likes}, 'e', {engagement} )
    print (dbg_txt)
    print('f1', type(foto1_likes), 'f2', type(foto2_likes), 'f3', type(foto3_likes))
    print('c', type(comentarios_total))
    print('g', type(guardados_total))
    print('s', type(seguidores))
    print (dbg_txt)
    
#VARIABLES
seguidores = float('586') #dejar en flotante si NO interpreta que debe ser un numero exacto
foto1_likes = int('15')
foto2_likes = int('20')
foto3_likes = int('25')
#nuevo anadido
comentarios_total = int('0')
guardados_total = int('1')

#convertir a int
## no deja establecer una funcion de una

## operaciones de engagement
total_img_likes = int(foto1_likes) + int(foto2_likes) + int(foto3_likes)
#engagement = total_img_likes * 5 / seguidores
#nueva formula corregida
test_engagement_suma = total_img_likes + comentarios_total + guardados_total
test_engagement_suma_y_div = (total_img_likes + comentarios_total + guardados_total) / seguidores
engagement = ((total_img_likes + comentarios_total + guardados_total) / seguidores) * 100

#print ("Puerta 18") DESDE FUNCION DE VARIABLES_PLACE
Nombre_Inst()
#FECHA v2
##ahora.day ahora.month ahora.year | ahora.hour ahora.minute ahora.second
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))
#
print ("-------------------------------------------")
print ("Calculadora de Engagement")
print ("===========================================")
#print ("")
print ("<b>Ejemplo:</b>", seguidores, "seguidores", total_img_likes, "likes en ultimas 3 fotos", "y", guardados_total, "guardado")
print ("<b>Engagement:</b>", engagement)
print ("===========================================")
#DESACTIVADA VERSION VIEJA DEL CALCULO
#Nueva Formula (no usa valores de 50 como ref)

## PROBAR res de funciones and y or en donde dice and

# AND NO es lo mismo que & (operadores de bit)
# OR NO es lo mismo que | (operadores de bit)

Calc_Engmnt()

print ("===========================================")
print ("valores de prueba:", "suma=", test_engagement_suma, "total", "y da", test_engagement_suma_y_div, "dividido por los seguidores") 
print ("===========================================")
# ANADIR MODO MANUAL

## ANADIR EVALUACION SEGUN INPUT (MENU DE OPCIONES AUTOMATIZADA CON API O MANUAL)

# RESET VALUES
seguidores = None 
foto1_likes = None 
foto2_likes = None 
foto3_likes = None 
comentarios_total = None 
guardados_total = None 
total_img_likes = None
engagement = None

#read var
##DEBUG
#Debug()

#
print ("Ingrese los valores del perfil de instagram a comprobar:")
#seguidores
#likes foto1
while True:
    foto1_likes = input("Ingresa likes de la primer foto:")
    #   check si es numero o string:
    try:
        val = int(foto1_likes)
        break
    except ValueError:
        try:
            float(foto1_likes)
            print('no se aceptan flotantes.')
        except ValueError:
            print("NO es un numero.")
#likes foto2
#convertir a entero
foto1_likes = int(foto1_likes)
## foto2_likes = int(input("Ingresa likes de la segunda foto:"))
while True:
    foto2_likes = input("Ingresa likes de la segunda foto:")
    #   check si es numero o string:
    try:
        val = int(foto2_likes)
        break
    except ValueError:
        try:
            float(foto2_likes)
            print('no se aceptan flotantes.')
        except ValueError:
            print("NO es un numero.")
#likes foto3
#convertir a entero
foto2_likes = int(foto2_likes)
#foto3_likes = int(input("Ingresa likes de la tercer foto:"))
while True:
    foto3_likes = input("Ingresa likes de la tercer foto:")
    #   check si es numero o string:
    try:
        val = int(foto3_likes)
        break
    except ValueError:
        try:
            float(foto3_likes)
            print('no se aceptan flotantes.')
        except ValueError:
            print("NO es un numero.")
#SUMAR
#convertir a entero
foto3_likes = int(foto3_likes)
total_img_likes = foto1_likes + foto2_likes + foto3_likes
#nuevo anadido
#comentarios
#comentarios_total = int(input("Ingresa total de comentarios fotos (en caso de no haber, llenar con cero):"))
while True:
    comentarios_total = input("Ingresa total de comentarios fotos (en caso de no haber, llenar con cero):")
    #   check si es numero o string:
    try:
        val = int(comentarios_total)
        break
    except ValueError:
        try:
            float(comentarios_total)
            print('no se aceptan flotantes.')
        except ValueError:
            print("NO es un numero.")
#guardados_total = int(input("Ingresa total de guardados (en caso de no haber, llenar con cero):"))
comentarios_total = int(comentarios_total)
while True:
    guardados_total = input("Ingresa total de guardados (en caso de no haber, llenar con cero):")
    #   check si es numero o string:
    try:
        val = int(guardados_total)
        break
    except ValueError:
        try:
            float(guardados_total)
            print('no se aceptan flotantes.')
        except ValueError:
            print("NO es un numero.")
#seguidores
#seguidores = int(input("Ingresa cantidad de seguidores:"))
guardados_total = int(guardados_total)
while True:
    seguidores = input("Ingresa cantidad de seguidores:")
    #   check si es numero o string:
    try:
        val = int(seguidores)
        break
    except ValueError:
        try:
            float(seguidores)
            print('no se aceptan flotantes.')
        except ValueError:
            print("NO es un numero.")
seguidores = int(seguidores)
#Debug()
#resultado ingreso manual manual
engagement = ((total_img_likes + comentarios_total + guardados_total) / seguidores) * 100

#DESACTIVADA VERSION VIEJA DEL CALCULO
##Nueva Formula (no usa valores de 50 como ref)

Calc_Engmnt()

print ("===========================================")
print ("El engagement es:", engagement)
print ("===========================================")
#FECHA v2
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))
#
#read var
##DEBUG 
#nota 2.3: activar para ver datos en memoria
#Debug()
