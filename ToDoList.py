#https://www.javatpoint.com/simple-to-do-list-gui-application-in-python

#Importar los modulos necesarios para el proyecto

import tkinter as tk            #importa modulo tkinter como tk
from tkinter import ttk         #importa modulo ttk de la libreria de tkinter
from tkinter import messagebox  #importa el modulo messagebox de tkinter

import sqlite3 as sql 

###################################################################
#Definir las funciones necesarias para ejecutar la aplicacion

task = []                       #Definir una lista vacia

#Funcion agregar tarea

def add_task(task_field):                       
    task_string = task_field.get()              #Consigue string del campo entrante
    
    if len(task_string)==0:                     #Revisa si el string esta vacio
        messagebox.showinfo("Error", "Field is Empty")  #Muestra message box con "Field is empty"
    else:
        task.append(task_string)                #Agrega el string a la lista de tareas
        the_cursor.execute("Insert into tak values(?)",(task_string)) #usando el metodo execute() para ejecutar una instancia de SQL
        list_update()                       #Funcion para actualizar la lista
        task_field.delete(0,"end")

#Funcion para actualizar la lista

def list_update(): 
    clear_list()                           #Limpiar la lista

    for task in tasks:  
        task_listbox.insert("end",task)    #usar el metodo insert() para agregar tareas


#Funcion para borrar tarea de la lista

def delete_task():
    try:
        the_value=task_listbox.get(task_listbox.curselection())


#Crear un form para la aplicacion
#Agregar base de datos 
#Widgets y triggers 
#Llamar a las funciones