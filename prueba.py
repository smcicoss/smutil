#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ·
#
"""
=====================================================================
                                prueba
=====================================================================
Autor:  Simón Martínez <simon@cicoss.net>
fecha:  dom dic  6 00:07:32 CET 2020
---------------------------------------------------------------------

script para la prueba y demostración de los módulos smutil

"""
import os
from utiles.color import Color
from utiles.strutil import dehumanize
# from utiles.menu import Menu

if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

# --
'''
TODO:
tipos de dialogos
__type = ('menu', 'text', 'url', 'email', 'password', 'number',
          'datetime', 'date', 'time')

'''

color = Color()

print(f"{color.doc}\n{color}")

print(f"{color.ROJO}algo en rojo{color.END}\n\n")

siz = "365,4GB"
print(f"{siz:9} = {color.VERDE}{dehumanize(siz)}{color.END}")
siz2 = "365,4GiB"
print(f"{siz2:9} = {color.MARRON}{dehumanize(siz2)}{color.END}")
siz3 = "365.4G"
print(f"{siz3:9} = {color.PURPURA}{dehumanize(siz3)}{color.END}")
