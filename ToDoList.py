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
        the_cursor.execute("Insert into task values(?)",(task_string)) #usando el metodo execute() para ejecutar una instancia de SQL
        list_update()                       #Funcion para actualizar la lista
        task_field.delete(0,"end")



##Funcion para actualizar la lista

def list_update(): 
    clear_list()                           #Limpiar la lista

    for task in tasks:  
        task_listbox.insert("end",task)    #usar el metodo insert() para agregar tareas




##Funcion para borrar tarea de la lista

def delete_task():
    
    try:
        the_value = task_listbox.get(task_listbox.curselection())             #consigue la entrada seleccionada desde la list box

        if the_value in tasks:
            task.remove(the_value)          #Elimina la tarea de la lista
            list_update()                   #Llamo a la funcion actualizar lista
            the_cursor.execute('delete from task where title =?',(the_value))
    except:
        messagebox.showinfo("Error","No esta la tarea seleccionada. No se puede borrar")



##Funcion para borrar toda las tareas de la lista

def delete_all_task():          #Defino funcion
    message_box = messagebox.askyesno("Borrar todo","Estas seguro?")    #Despliego mensaje preguntando al usuario para confirmacion
    if message_box == True:
        while(len(task)!=0):            #usar un loop de while hasta que no haya elementos en la lista
            task.pop()                  #Usando el metodo pop() popea los elementos de la misma.
        the_cursos.execute("delete from task")
        list_update()



##Funcion para limpiar lista

def clear_list():
    task_listbox.delete(0,"end")        #borrar todas las entradas de la lista con el metodo delete


##Funcion para cerrar la aplicacion

def close():
    print(task)     #imprimir los elementos de la lista de tareas 
    guiWindows.destroy()  #usando el metodo destroy() cerramos la aplicacion


##Funcion para recuperar los datos de la base de datos

def retrieve_database():
    while(len(tasks)!=0):       #usando el metodo pop() popea todos los elementos de la lista
        task.pop()
    for row in the_curso.execute("select title from tasks"): #iterar por los rows en la base de datos
        tasks.append(row[0])

#############################################################################################
#Crear un form para la aplicacion

#main function

if __name__=="__name__":
    guiWindows = tk.Tk()            #crear un objeto de la clase Tk()
    guiWindows.title("To-Do List Manager - JAVAPOINT") #Setear titulo
    guiWindows.geometry("500x500+750+250") #Setear geometria de la ventana
    guiWindows.resizable(0,0)   #Deshabilitar la opcion de redimensionado
    guiWindows.configure(bg="#FAEBD7") #Setear el fondo 

#Agregar base de datos 

the_connection = sql.connect("listOfTasks.db")  #usando el metodo connect() conectamos a la base de datos
the_cursor = the_connection.cursor              #Creamos un objeto de la clase cursor
the_cursor.execute("create table if not exist taks(title text)")
prueba
#Widgets y triggers 
#Llamar a las funciones