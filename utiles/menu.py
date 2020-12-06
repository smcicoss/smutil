# -*- coding: utf-8 -*-
# ·
#
"""
=====================================================================
                                Menu
=====================================================================
autor:  Simón Martínez <simon@cicoss.net>
fecha:  dom dic  6 00:01:20 CET 2020
---------------------------------------------------------------------

Clase para la creación y ejecución de un menú interactivo
en consola.

"""


class Menu:
    def __init__(self):
        self.title = None
        self.help = None
        self.prompt = None
        self.__width = 0
        # __options = [{'name': "", 'def': "", 'help': ""}]
        self.__options = []
        self.__type = None

    def presenta(self):
        pass

    def add_option(self, value):
        if value is None:
            return

        if type(value) == 'str':
            self.__options.append(value)
