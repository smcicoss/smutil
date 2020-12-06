# -*- coding: utf-8 -*-
# ·
#
"""
=====================================================================
                            strutil
=====================================================================
autor:  Simón Martínez <simon@cicoss.net>
fecha:  dom dic  6 19:01:07 CET 2020
---------------------------------------------------------------------

Modulo de definición de fuciones útiles sobre str

"""
import re


def dehumanize(str_human):
    """
    dehumanize deshumaniza

    Convierte string de Números con formato humanizado en enteros

    Args:
        str_human (str): cadena con formato humanizado
                         K,KIB,M,MiB,G,GiB,T,TiB potencias de 2
                         KB,MB,GB,TB potencias de 10

    Returns:
        int: valor entero
    """
    # TODO: añadir formatos de multiplos internacionales
    #       KB, MB, GB, TB potencias de 10

    # patron = "^[0-9]+?(\.[0-9]{3})? ?(KiB|K|k)$"
    patron10 = " ?(KB|MB|GB|TB){1}$"
    patron2 = " ?(KiB|K|MiB|M|GiB|G|TiB|T){1}$"
    prog2 = re.compile(patron2)
    prog10 = re.compile(patron10)
    str_human = str_human.replace(',', '.')
    match = prog2.search(str_human)
    if match is not None:
        pos = match.regs[0][0]
        numero = str_human[0:pos].strip()
        pot = str_human[pos:].strip()
        if pot[0] == 'K':
            mult = 2**10
        elif pot[0] == 'M':
            mult = 2**20
        elif pot[0] == 'G':
            mult = 2**30
        else:
            mult = 2**40

        try:
            return round(float(numero) * mult)

        except ValueError:
            return None
    else:
        match = prog10.search(str_human)
        if match is not None:
            pos = match.regs[0][0]
            numero = str_human[0:pos].strip()
            pot = str_human[pos:].strip()
            if pot[0] == 'K':
                mult = 10**3
            elif pot[0] == 'M':
                mult = 10**6
            elif pot[0] == 'G':
                mult = 10**9
            else:
                mult = 10**12

            try:
                return round(float(numero) * mult)

            except ValueError:
                return None
        else:
            try:
                return round(float(str_human))
            except ValueError:
                return None
