# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:33:19 2025

@author: DELL
"""

try:
    f= open('comida.txt', 'rt');
    plato =f.readline();
    print(plato);
    f.close();

except IOError:
    print('Un error fichero no encontrado');

except OSError:
    print('Error usando el fichero');
