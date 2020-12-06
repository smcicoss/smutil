# -*- coding: utf-8 -*-
# ·
#
"""
=====================================================================
                                color
=====================================================================
autor:  Simón Martínez <simon@cicoss.net>
fecha:  dom dic  6 10:40:51 CET 2020
---------------------------------------------------------------------

códigos de escape para la salida de color por consola

"""


class Color:
    """
     Clase Color

    genera los códigos de escape para la salida de texto de color
    """
    def __init__(self):
        """
        __init__ Constructor

        Define las variables internas
        """
        self.__escapecolor = "\033["
        self.__separador = ";"
        self.__terminador = "m"

        self.__lumin = {'normal': "0", 'intenso': "1"}
        self.__plano = {'letra': "3", 'fondo': "4"}
        self.__color = {
            'negro': "0",
            'rojo': "1",
            'verde': "2",
            'marron': "3",
            'azul': "4",
            'purpura': "5",
            'cian': "6",
            'gris': "7"
        }

        # vuelve al color por defecto
        self.__END = "\033[0m"

    def __composer(self, letra=None, fondo=None, lumin=None):
        """
        __composer letra, fondo, luminosidad

        Genera el código en función de los tres parámetros

        Args:
            letra (str, optional): Nombre del color de la letra.
                                    Defaults to None.
            fondo (str, optional): Nombre del color del fondo.
                                    Defaults to None.
            lumin (str, optional): Intensidad 'normal' o 'intenso'.
                                    Defaults to None.

        Returns:
            str: código compuesto
        """
        if lumin is None and letra is None and fondo is None:
            # Si no se pasa ningun parametro o los tres None
            # devuelve el codigo de cierre
            return self.__END

        # secuencia de escape para color
        code = self.__escapecolor

        if lumin is not None:
            # Establece la luminosidad 'normal' o 'intenso'
            code += self.__lumin[lumin]
        if letra is not None:
            if code[-1] != "[":
                code += self.__separador
            code += self.__plano['letra'] + self.__color[letra]
        if fondo is not None:
            if code[-1] != "[":
                code += self.__separador
            code += self.__plano['fondo'] + self.__color[fondo]

        code += self.__terminador

        return code

    def compone(self, letra=None, fondo=None, lumin=None):
        """
        compone interface para self_composer

        Chequeo previo de los valores

        Args:
            los mismos que en __composer

        Returns:
            str: el código
            None: Mal parámetro
        """
        if letra not in [None, self.colores]:
            return None
        if fondo not in [None, self.colores]:
            return None
        if lumin not in [None, self.__lumin]:
            return None

        return self.__composer(letra, fondo, lumin)

    def __str__(self):
        """
        __str__ string del objeto

        Compone una muestra de colores y de nombres

        Returns:
            str: la Muestra
        """
        str = f"Colores disponibles: {self.colores}\n"
        str += f"Intensidades disponibles: {self.intensidades}\n\n"

        for fondo in self.colores:
            for int in self.intensidades:
                for letra in self.colores:
                    str += f"{self.__composer(letra, fondo, int)}"
                    muestra = f"letra {letra} "
                    muestra += f"{int} sobre fondo {fondo}"
                    str += f"{muestra:^46}{self.__END}\n"

        str += f"\n{self.ERROR}ERORR{self.__END}\n"
        str += f"{self.WARNING}WARNING{self.__END}\n"
        str += f"{self.ALERTA}ALERTA{self.__END}\n"
        str += f"{self.OK}OK{self.__END}\n"
        str += f"{self.PROMPT}PROMPT{self.__END}\n"
        str += f"{self.DESTACA}DESTACA{self.__END}\n"

        str += f"{self.__END}END\n\n"

        str += f"{self.NEGRO}NEGRO{self.__END}\n"
        str += f"{self.ROJO}ROJO{self.__END}\n"
        str += f"{self.VERDE}VERDE{self.__END}\n"
        str += f"{self.MARRON}MARRON{self.__END}\n"
        str += f"{self.AZUL}AZUL{self.__END}\n"
        str += f"{self.PURPURA}PURPURA{self.__END}\n"
        str += f"{self.CIAN}CIAN{self.__END}\n"
        str += f"{self.GRIS}GRIS{self.__END}\n"
        str += f"{self.AMARILLO}AMARILLO{self.__END}\n"
        str += f"{self.BLANCO}BLANCO{self.__END}\n"

        str += f"{self.__END}END\n"

        return str

    @property
    def colores(self):
        return list(self.__color.keys())

    @property
    def intensidades(self):
        return list(self.__lumin.keys())

    @property
    def planos(self):
        return list(self.__plano.keys())

    @property
    def END(self):
        return self.__END

    @property
    def ERROR(self):
        return self.__composer('rojo', 'negro', 'intenso')

    @property
    def WARNING(self):
        return self.__composer('marron', 'negro', 'normal')

    @property
    def ALERTA(self):
        return self.__composer('marron', 'azul', 'intenso')

    @property
    def OK(self):
        return self.__composer('verde', 'negro', 'normal')

    @property
    def PROMPT(self):
        return self.__composer('gris', 'negro', 'intenso')

    @property
    def DESTACA(self):
        return self.__composer('marron', 'negro', 'intenso')

    @property
    def NEGRO(self):
        return self.__composer('negro', None, 'normal')

    @property
    def ROJO(self):
        return self.__composer('rojo', None, 'normal')

    @property
    def VERDE(self):
        return self.__composer('verde', None, 'normal')

    @property
    def MARRON(self):
        return self.__composer('marron', None, 'normal')

    @property
    def AZUL(self):
        return self.__composer('azul', None, 'normal')

    @property
    def PURPURA(self):
        return self.__composer('purpura', None, 'normal')

    @property
    def CIAN(self):
        return self.__composer('cian', None, 'normal')

    @property
    def GRIS(self):
        return self.__composer('gris', None, 'normal')

    @property
    def AMARILLO(self):
        return self.__composer('marron', None, 'intenso')

    @property
    def BLANCO(self):
        return self.__composer('gris', None, 'intenso')

    @property
    def doc(self):
        return self.__doc__
