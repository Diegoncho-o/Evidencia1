#Sistema de Gestion de Empleados

#Variables de alcance global

num_empleado = 0
nom_empleado = ""
nom_departamento = ""
monto_salario = 0.00

#Diccionarios

Nombre={}
Departamento={}
Salario={}

# La funcion Alta_Empleados nos servira para agregar empleados
def Alta_Empleados ():
    while True:   # Ciclo principal
        print(f" * Sistema de Gestion de Empleados * ")
        print(f"")
        print(f" * Alta de Empleados *")
        print(f"")
        num_empleado=int(input("Numero del Empleado: "))
        
        if ((num_empleado in Nombre) and (num_empleado in Departamento) and (num_empleado in Salario)):
            print(f"")
            print(f"El empleado {num_empleado} ya existe !!")
            print(f"")
            continue
        
        # El empleado todavia no existe
        nom_empleado=input("Nombre del Empleado: ")
        nom_departamento=input("Nombre de Departamento: ")
        monto_salario=float(input("Salario: "))
        
        
        while True:  # Ciclo de la pregunta al usuario
            print(f"")
            datos_correctos=str(input("¿Los datos estan correctos? (S/N) "))
        
            if (datos_correctos != "N" and datos_correctos != "S"):
               continue  # Regresa al inicio del ciclo de la pregunta
            
            break  # Se sale del ciclo de la pregunta
        
        # Aqui se salio del ciclo de la pregunta
        if (datos_correctos == "N"):
            continue # Regresa al ciclo principal
        
        # El usuario respondio datos_correctos == "S" 
        Nombre[num_empleado]= nom_empleado
        Departamento[num_empleado]= nom_departamento
        Salario[num_empleado]= monto_salario
        
        print(f"")
        print(f" El empleado ha sido dado de alta" )
        
        while True:  # Ciclo de la pregunta al usuario
            print(f"")
            pregunta=str(input("¿Desea agregar otro empleado? (S/N) "))
            print(f"")
            
            if (pregunta != "N" and pregunta != "S"):
               continue  # Regresa al inicio del ciclo de la pregunta
            
            break  # Se sale del ciclo de la pregunta
        
        # Aqui se salio del ciclo de la pregunta
        if (pregunta == "S"):
            continue  # Regresa a ciclo principal
        
        # Aqui la respuesta del usuario a la pregunta es == "N"
        break  # Regresara al menu principal

def Actualizar_Empleados ():
    while True:   # Ciclo principal
        print(f" * Sistema de Gestion de Empleados * ")
        print(f"")
        print(f" * Actualizacion de Empleados * ")
        print(f"")
        num_empleado=int(input("Numero del Empleado:  "))
        print(f"")
        
        if ((num_empleado in Nombre) and (num_empleado in Departamento) and (num_empleado in Salario)): # El empleado si existe
            nom_empleado=Nombre.get(num_empleado)
            nom_departamento=Departamento.get(num_empleado)
            monto_salario=float(Salario.get(num_empleado))
            
            print(f"Nombre del Empleado: {nom_empleado} ")
            print(f"Departamento del Empleado: {nom_departamento} ")
            print(f"Salario del Empleado: ${monto_salario:,.2f} ")
            
            while True:  # Ciclo de la pregunta al usuario
                print(f"")
                pregunta=str(input(" ¿Desea actualizar los datos de este empleado? (S/N) "))
                print(f"")
                
                if (pregunta != "N" and pregunta != "S"):
                    continue  # Regresa al inicio del ciclo de la pregunta
                
                break  # Se sale del ciclo de la pregunta
            
            # Aqui se salio del ciclo de la pregunta
            if (pregunta == "N"):
                break   # Se sale del ciclo principal y regresa al menu principal
            
            # El usuario respondio pregunta == "S"
            nom_empleado=input("Nombre del Empleado: ")
            nom_departamento=input("Nombre de Departamento: ")
            monto_salario=float(input("Salario: "))
            
            Nombre[num_empleado] = nom_empleado
            Departamento[num_empleado] = nom_departamento
            Salario[num_empleado] = monto_salario
            
            print(f"")
            print(f"Los datos del empleado se han actualizado")
            
            while True:  # Ciclo de la pregunta al usuario
                print(f"")
                pregunta=str(input(" ¿Desea actualizar otro empleado? (S/N) "))
                print(f"")
                
                if (pregunta != "N" and pregunta != "S"):
                    continue  # Regresa al inicio del ciclo de la pregunta
                
                break # Se sale del ciclo de la pregunta
            
            # Aqui se salio del ciclo de la pregunta
            if (pregunta == "S"):
                continue # Regresa al ciclo principal
            
        else:
            print(f"El empleado {num_empleado} no existe !!")
            print(f"")
            continue # Regresa al ciclo principal
            
        break  # Regresara al menu principal
    
def Consulta_Empleados ():
    while True:   #Ciclo principal
        print(f" * Sistema de Gestion de Empleados * ")
        print(f"")
        print(f" * Consulta de Empleados * ")
        print(f"")
        num_empleado=int(input("Numero del Empleado:  "))
        print(f"")
        
        if ((num_empleado in Nombre) and (num_empleado in Departamento) and (num_empleado in Salario)): # El empleado si existe
            nom_empleado=Nombre.get(num_empleado)
            nom_departamento=Departamento.get(num_empleado)
            monto_salario=float(Salario.get(num_empleado))
            
            print(f"Nombre del Empleado: {nom_empleado} ")
            print(f"Departamento del Empleado: {nom_departamento} ")
            print(f"Salario del Empleado: ${monto_salario:,.2f} ")
            
            while True:  # Ciclo de la pregunta al usuario
                print(f"")
                pregunta=str(input(" ¿Desea consultar otro empleado? (S/N) "))
                print(f"")
                
                if (pregunta != "N" and pregunta != "S"):
                    continue  # Regresa al inicio del ciclo de la pregunta
                
                break  # Se sale del ciclo de la pregunta
            
            # Aqui se salio del ciclo de la pregunta
            if (pregunta == "S"):
                continue  # Regresa al ciclo principal
            
        else:
            print(f"El empleado {num_empleado} no existe !!")
            print(f"")
            continue  # Regresa al ciclo principal
            
        break  # Regresara al menu principal
                
def Baja_Empleados ():
    while True:   # Ciclo principal
        print(f" * Sistema de Gestion de Empleados * ")
        print(f"")
        print(f" * Baja de Empleados *")
        print(f"")
        num_empleado=int(input("Numero del Empleado: "))
        print(f"")
        
        if ((num_empleado in Nombre) and (num_empleado in Departamento) and (num_empleado in Salario)): # El empleado si existe
            nom_empleado=Nombre.get(num_empleado)
            nom_departamento=Departamento.get(num_empleado)
            monto_salario=float(Salario.get(num_empleado))
            
            print(f"Nombre del Empleado: {nom_empleado} ")
            print(f"Departamento del Empleado: {nom_departamento} ")
            print(f"Salario del Empleado: ${monto_salario:,.2f} ")
            
            while True:  # Ciclo de la pregunta al usuario
                print(f"")
                pregunta=str(input("¿Deseas dar de baja a este empleado? (S/N) "))
                print(f"")
            
                if (pregunta != "N" and pregunta != "S"):
                   continue  # Regresa al inicio del ciclo de la pregunta 
                
                break  # Se sale del ciclo de la pregunta
            
            # Aqui se salio del ciclo de la pregunta
            if (pregunta == "N"):
                break  # Se sale del ciclo principal y regresa al menu principal
            
            #El usuario respondio pregunta == "S"
            Nombre.pop(num_empleado)
            Departamento.pop(num_empleado)
            Salario.pop(num_empleado)
            
            print(f"")
            print(f" El empleado ha sido dado de baja ")
            
            while True:  # Ciclo de la pregunta al usuario
                print(f"")
                pregunta=str(input("¿Desea borrar otro empleado? (S/N) "))
                print(f"")
                
                if (pregunta != "N" and pregunta != "S"):
                   continue  # Regresa al inicio del ciclo de la pregunta
                
                break # Se sale del ciclo de la pregunta
            
            # Aqui se salio del ciclo de la pregunta
            if (pregunta == "S"):
                continue  # Regresa al ciclo principal
        
        else:
            print(f"El empleado {num_empleado} no existe !!")
            print(f"")
            continue # Regresa al ciclo principal
                
        break  # Regresara al menu principal
    
def Salario_Total ():
    print(f" * Sistema de Gestion de Empleados * ")
    print(f"")
    print(f" * Consulta Salario Total * ")
    print(f"")
    
    salario_total = 0.00 
    
    print(f" Empleado , Nombre , Departamento , Salario ")
    print(f"")
    
    for num_empleado in Nombre: # Ciclo para obtener las llaves del diccionario "Nombre", el valor de la llave se guarda en "num_empleado"
        nom_empleado=Nombre.get(num_empleado)
        nom_departamento=Departamento.get(num_empleado)
        monto_salario=float(Salario.get(num_empleado))
        
        salario_total=salario_total + monto_salario
        
        print(f" {num_empleado} , {nom_empleado} , {nom_departamento} , ${monto_salario:,.2f} ")
                          
    print(f"")
    print(f"El salario total es: ${salario_total:,.2f} ")
    print(f"")
    
    while True:  # Ciclo de la pregunta al usuario
        pregunta=str(input("Presione [T] para terminar la consulta: "))
        print(f"")
        
        if (pregunta != "T"):
            continue  # Regresa al inicio del ciclo de la pregunta
        
        break # Se sale del ciclo de la pregunta y regresa al menu principal
     
     
# Programa principal
    
while True:
    print(f" * Sistema de Gestion de Empleados * ")
    print(f"")

    print(f" 1 - Agregar Empleados")
    print(f" 2 - Actualizar Empleados")
    print(f" 3 - Consultar Empleados")
    print(f" 4 - Borrar Empleados")
    print(f" 5 - Consulta Salario Total")
    print(f" 6 - Salir")
    print(f"")

    num_opcion=int(input("Ingresa la opcion: "))

    if (num_opcion == 1):
        Alta_Empleados()
        continue
    elif (num_opcion == 2):
        Actualizar_Empleados()
        continue
    elif (num_opcion == 3):
        Consulta_Empleados()
        continue
    elif (num_opcion == 4):
        Baja_Empleados()
        continue
    elif (num_opcion == 5):
        Salario_Total()
        continue
    elif (num_opcion == 6):
        print(f"")
        print(f" Gracias por utilizar el Sistema")
        break
    else:
        print(f" Opcion Invalida")
        print(f"")
        continue

# Aqui termina el programa principal





















