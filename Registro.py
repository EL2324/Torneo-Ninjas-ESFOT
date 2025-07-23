import tkinter as tk 
from tkinter import messagebox
import random
import os 

#--------------Guardar_Archivo----------------------------------

def guardar_ganador(nombre, archivo="ganadores1vs1.txt"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(nombre + "\n")
