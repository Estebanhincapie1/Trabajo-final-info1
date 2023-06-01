import mysql.connector
from datetime import datetime

def conexion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
    )   
    return mydb

def validar_usuario():
    # Establecer la conexión a la base de datos
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        print("Bienvenido al sistema de gestión de medicamentos, por favor inicie sesión para continuar")
        usuario = input("Ingrese el nombre de usuario: ")  
        pwrd = input("Ingrese la contraseña: ")
        # consulta para buscar el usuario en la base de datos
        sql = "SELECT * FROM usuarios WHERE username = %s AND password =%s"
        mycursor.execute(sql, (usuario, pwrd))

        # Obtener el resultado de la consulta
        resultado = mycursor.fetchone()

        # Validar si se encontró el usuario en la base de datos
        if resultado:
            print("Inicio de sesión exitoso")
            menu()
            break
        else:
            print("Información incorrecta, intente de nuevo")


def menu():
    while True:
        print("\n--- Menú de gestión de Fármacos ---")
        print("1. Ingresar al menú de Medicamentos")
        print("2. Ingresar al menú de Proveeedores")
        print("3. Ingresar al menú de Ubicaciones")
        print("4. Salir del sistema")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_medicamentos()
        elif opcion == "2":
            menu_proveedores()
        elif opcion == "3":
            menu_ubicaciones()
        elif opcion == "4":
            print("--- Saliendo del sistema ---")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def menu_medicamentos():
    print("\n--- Menú de gestión de Medicamentos ---")
    print("1. Ingresar un nuevo Medicamento")
    print("2. Actualizar la información de un Medicamento")
    print("3. Buscar un Medicamento")
    print("4. Ver la información de todos los medicamentos almacenados")
    print("5. Eliminar un Medicamento")
    print("6. Volver al menú principal")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_medicamento()
    elif opcion == "2":
        actualizar_medicamento()
    elif opcion == "3":
        buscar_medicamento()
    elif opcion == "4":
        ver_medicamentos()
    elif opcion == "5":
        eliminar_medicamento()
    elif opcion == "6":
        print("--- Saliendo del menú de medicamentos ---")
        menu()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_medicamentos()

def ingresar_medicamento():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    print("\n---  Ingrese la información de el Medicamento ---")
    lote = input("Ingrese el lote del medicamento: ")
    medname = input("Ingrese el nombre del medicamento: ")
    distribuidor = input("Ingrese el distribuidor del medicamento: ")
    while True:
        qtty = input("Ingrese la cantidad actualizada del medicamento sin puntos ni comas: ")
        if qtty.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo") 
            continue   
    while True:
        doarrival = input("Ingrese la fecha de llegada del medicamento en formato dd-mm-aaaa: ")
        try:
            fecha_llegada = datetime.strptime(doarrival, "%d-%m-%Y")
            break 
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")
    while True:
        precioventa = input("Ingrese el nuevo precio de venta del medicamento sin puntos ni comas: ") 
        if precioventa.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo") 
    sql = "INSERT INTO medicamentos (LOTE, NOMBRE, DISTRIBUIDOR, CANTIDAD, LLEGADA, PRECIOVENTA) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (lote, medname, distribuidor, qtty, fecha_llegada, precioventa)
    mycursor.execute(sql, valores)
    mydb.commit()
    print("---- Medicamento agregado con exito ----")
    while True:
        respuesta = input("¿Desea agregar otro medicamento? Si responde no, será llevado de vuelta al menú de los medicamentos (s/n): ")
        if respuesta.lower() == 's':
            ingresar_medicamento()
            break
        elif respuesta.lower() == 'n':
            menu_medicamentos()  
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")

def actualizar_medicamento():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        lote = input("Ingrese el lote del medicamento que desea actualizar: ")
        sql_verif = ("SELECT * FROM medicamentos WHERE LOTE = %s")
        mycursor.execute(sql_verif, (lote,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El lote ingresado no existe en la base de datos. Intente nuevamente.")
    while True:
        qtty = input("Ingrese la cantidad actualizada del medicamento sin puntos ni comas: ")
        if qtty.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo")            
    while True:
        doarrival = input("Ingrese la nueva fecha de llegada del medicamento en formato dd-mm-aaaa: ")
        try:
            fecha_llegada = datetime.strptime(doarrival, "%d-%m-%Y")
            break 
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")
    while True:
        precioventa = input("Ingrese el nuevo precio de venta del medicamento sin puntos ni comas: ") 
        if precioventa.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo")   
    sql = "UPDATE medicamentos SET CANTIDAD = %s, LLEGADA = %s, PRECIOVENTA = %s WHERE LOTE = %s"
    valores = (qtty, fecha_llegada, precioventa, lote)
    mycursor.execute(sql, valores)
    mydb.commit()
    while True:
        respuesta = input("¿Desea actualizar otro medicamento? Si responde no, será llevado de vuelta al menú de los medicamentos (s/n): ")
        if respuesta.lower() == 's':
            actualizar_medicamento()
            break
        elif respuesta.lower() == 'n':
            menu_medicamentos()
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")
            continue  

def buscar_medicamento():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        lote = input("Ingrese el lote del medicamento que desea buscar: ")
        sql_verif = ("SELECT * FROM medicamentos WHERE LOTE = %s")
        mycursor.execute(sql_verif, (lote,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El lote ingresado no existe en la base de datos. Intente nuevamente.")
            continue
    print("\nInformación del medicamento:")
    print("Lote:", resultado[0])
    print("Nombre:", resultado[1])
    print("Distribuidor:", resultado[2])
    print("Cantidad:", resultado[3])
    print("Fecha de llegada:", resultado[4])
    print("Precio de venta:", resultado[5])
    while True:
        respuesta = input("¿Desea buscar otro medicamento? Si responde no, será llevado de vuelta al menú de los medicamentos (s/n): ")
        if respuesta.lower() == 's':
            break
        elif respuesta.lower() == 'n':
            menu_medicamentos()
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")

def ver_medicamentos():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM medicamentos")
    resultados = mycursor.fetchall()
    print("\nInformación de los medicamentos:")
    for medicamento in resultados:
        print("Lote:", medicamento[0])
        print("Nombre:", medicamento[1])
        print("Distribuidor:", medicamento[2])
        print("Cantidad:", medicamento[3])
        print("Fecha de llegada:", medicamento[4])
        print("Precio de venta:", medicamento[5])
        print("-------------------------")
    while True:
        respuesta = input("Presione 'r' para regresar al menú principal de medicamentos: ")
        if respuesta.lower() == 'r':
            menu_medicamentos()
            break
        else:
            print("Opción no válida. Por favor, ingrese 'r' para regresar al menú principal.")


def eliminar_medicamento():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        lote = input("Ingrese el lote del medicamento que desea eliminar: ")
        sql_verif = ("SELECT * FROM medicamentos WHERE LOTE = %s")
        mycursor.execute(sql_verif, (lote,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El lote ingresado no existe en la base de datos. Intente nuevamente.")
    sql = "DELETE FROM medicamentos WHERE LOTE = %s"
    mycursor.execute(sql, (lote,))    
    mydb.commit()
    while True:
        respuesta = input("¿Desea eliminar otro medicamento? Si responde no, será llevado de vuelta al menú de los medicamentos (s/n): ")
        if respuesta.lower() == 's':
            break
        elif respuesta.lower() == 'n':
            menu_medicamentos()  
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")
    

def menu_proveedores():
    while True:
        print("\n--- Menú de gestión de Proveedores ---")
        print("1. Ingresar un nuevo Proveedor")
        print("2. Actualizar la información de un Proveedor")
        print("3. Buscar un Proveedor")
        print("4. Ver la información de todos los proveedores registrados")
        print("5. Eliminar un Proveedor")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_proveedor()
        elif opcion == "2":
            actualizar_proveedor()
        elif opcion == "3":
            buscar_proveedor()
        elif opcion == "4":
            ver_proveedor()
        elif opcion == "5":
            eliminar_proveedor()
        elif opcion == "6":
            print("--- Saliendo del menú de proveedores ---")
            menu()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue
        
def ingresar_proveedor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    print("\n---  Ingrese la información de el Proveedor ---")
    codigo = input("Ingrese el código del Proveedor: ")
    name = input("Ingrese el nombre del Proveedor: ")
    while not name.isalpha():
        name = input("El nombre debe contener solo letras. Ingrese nuevamente: ")
    lastname = input("Ingrese el apellido del Proveedor: ")
    while not lastname.isalpha():
        lastname = input("El apellido debe contener solo letras. Ingrese nuevamente: ")
    while True:
        cedula = input("Ingrese el número de documento de indetidad del proveedor sin puntos ni comas: ")
        if cedula.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo")    
    entity = input("Ingrese la entidad a la que pertenece el proceedor: ")
    while not entity.isalpha():
        entity = input("La entidad del proveedor debe contener solo letras. Ingrese nuevamente: ")
    sql = "INSERT INTO proveedores (CODIGO, NOMBRE, APELLIDO, ID, ENTIDAD) VALUES (%s, %s, %s, %s, %s)"
    valores = (codigo, name, lastname, cedula, entity)
    mycursor.execute(sql, valores)
    mydb.commit()
    print("---- Proveedor agregado con exito ----")
    while True:
        respuesta = input("¿Desea agregar otro Proveedor? Si responde no, será llevado de vuelta al menú de los proveedores (s/n): ")
        if respuesta.lower() == 's':
            ingresar_proveedor()
            break
        elif respuesta.lower() == 'n':
            menu_proveedores()  
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")

def actualizar_proveedor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        codigo = input("Ingrese el código del proveedor que desea actualizar: ")
        sql_verif = ("SELECT * FROM proveedores WHERE CODIGO = %s")
        mycursor.execute(sql_verif, (codigo,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El código ingresado no existe en la base de datos. Intente nuevamente.")
    name = input("Ingrese el nuevo nombre del Proveedor: ")
    while not name.isalpha():
        name = input("El nombre debe contener solo letras. Ingrese nuevamente: ")
    lastname = input("Ingrese el nuevo apellido del Proveedor: ")
    while not lastname.isalpha():
        lastname = input("El apellido debe contener solo letras. Ingrese nuevamente: ")
    while True:
        cedula = input("Ingrese el nuevo número de documento de indetidad del proveedor sin puntos ni comas: ")
        if cedula.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo")    
    entity = input("Ingrese la nueva entidad a la que pertenece el proceedor: ")
    while not entity.isalpha():
        entity = input("La entidad del proveedor debe contener solo letras. Ingrese nuevamente: ")
    sql = "UPDATE proveedores SET NOMBRE = %s, APELLIDO = %s, ID = %s, ENTIDAD = %s WHERE CODIGO = %s"
    valores = (name, lastname, cedula, entity, codigo)
    mycursor.execute(sql, valores)
    mydb.commit()
    while True:
        respuesta = input("¿Desea actualizar otro proveedor? Si responde no, será llevado de vuelta al menú de los proveedores (s/n): ")
        if respuesta.lower() == 's':
            actualizar_proveedor()
            break
        elif respuesta.lower() == 'n':
            menu_proveedores()
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")    

def buscar_proveedor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        codigo = input("Ingrese el código del proveedor que desea buscar: ")
        sql_verif = ("SELECT * FROM proveedores WHERE CODIGO = %s")
        mycursor.execute(sql_verif, (codigo,)) 
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El codigo ingresado no existe en la base de datos. Intente nuevamente.")
    print("\nInformación del proveedor:")
    print("Código:", resultado[0])
    print("Nombre:", resultado[1])
    print("Apellido:", resultado[2])
    print("Cédula:", resultado[3])
    print("Entidad:", resultado[4])
    while True:
        respuesta = input("¿Desea buscar otro proveedor? Si responde no, será llevado de vuelta al menú de los proveedores (s/n): ")
        if respuesta.lower() == 's':
            break
        elif respuesta.lower() == 'n':
            menu_proveedores()
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.") 

def ver_proveedor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM proveedores")
    resultados = mycursor.fetchall()
    print("\nInformación de los Proveedores:")
    for proveedor in resultados:
        print("Código:", proveedor[0])
        print("Nombre:", proveedor[1])
        print("Apellido:", proveedor[2])
        print("Cedula:", proveedor[3])
        print("Entidad:", proveedor[4])
        print("-------------------------")
    while True:
        respuesta = input("Presione 'r' para regresar al menú principal de proveedores: ")
        if respuesta.lower() == 'r':
            menu_proveedores()
            break
        else:
            print("Opción no válida. Por favor, ingrese 'r' para regresar al menú principal.")

def eliminar_proveedor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        codigo = input("Ingrese el codigo del proveedor que desea eliminar: ")
        sql_verif = ("SELECT * FROM proveedores WHERE CODIGO = %s")
        mycursor.execute(sql_verif, (codigo,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El codigo ingresado no existe en la base de datos. Intente nuevamente.")
    sql = "DELETE FROM proveedores WHERE CODIGO = %s"
    mycursor.execute(sql, (codigo,))    
    mydb.commit()
    print('Eliminado exitosamente')
    while True:
        respuesta = input("¿Desea eliminar otro proveedor? Si responde no, será llevado de vuelta al menú de los proveedores (s/n): ")
        if respuesta.lower() == 's':
            eliminar_proveedor()
            break
        elif respuesta.lower() == 'n':
            menu_proveedores()  
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")



def menu_ubicaciones():
    print("\n--- Menú de gestión de Ubicaciones ---")
    print("1. Ingresar una nueva Ubicación")
    print("2. Actualizar la información de una Ubicación")
    print("3. Buscar una Ubicación")
    print("4. Ver la información de todos las ubicaciones registradas")
    print("5. Eliminar una Ubicación")
    print("6. Volver al menú principal")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_ubicacion()
    elif opcion == "2":
        actualizar_ubicacion()
    elif opcion == "3":
        buscar_ubicacion()
    elif opcion == "4":
        ver_ubicacion()
    elif opcion == "5":
        eliminar_ubicacion()
    elif opcion == "6":
        print("--- Saliendo del menú de ubicaciones ---")
        menu()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_ubicaciones()



def ingresar_ubicacion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    print("\n---  Ingrese la información de la nueva Ubicación ---")
    while True:
        codigo = input("Ingrese el código de la Ubicación: ")
        if codigo.isalnum():
            break
        else:
            print("Formato incorrecto. Por favor intente nuevamente")
    name = input("Ingrese el nombre de la Ubicación: ")
    while not name.isalpha():
        name = input("El nombre debe contener solo letras. Ingrese nuevamente: ")
    while True:
        telf = input("Ingrese el número de teléfono de la ubicación sin agregar + como prefijo: ")
        if telf.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo")    
    sql = "INSERT INTO ubicaciones (CODIGO, NOMBREUBICACION, TELEFONO) VALUES (%s, %s, %s)"
    valores = (codigo, name, telf)
    mycursor.execute(sql, valores)
    mydb.commit()
    print("---- Ubicación agregada con exito ----")
    while True:
        respuesta = input("¿Desea agregar otra Ubicación? Si responde no, será llevado de vuelta al menú de las Ubicaciones (s/n): ")
        if respuesta.lower() == 's':
            ingresar_ubicacion()
            break
        elif respuesta.lower() == 'n':
            menu_ubicaciones()  
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")

def actualizar_ubicacion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        codigo = input("Ingrese el código de la ubicación que desea actualizar: ")
        sql_verif = ("SELECT * FROM ubicaciones WHERE CODIGO = %s")
        mycursor.execute(sql_verif, (codigo,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El código ingresado no existe en la base de datos. Intente nuevamente.")
    name = input("Ingrese el nuevo nombre de la ubicación: ")
    while not name.isalpha():
        name = input("El nombre debe contener solo letras. Ingrese nuevamente: ")
    while True:
        telf = input("Ingrese el nuevo número de telefono de la ubicación sin agregar + como prefijo: ")
        if telf.isdigit():
            break
        else:
            print("Formato incorrecto, intente de nuevo")    
    sql = "UPDATE ubicaciones SET NOMBREUBICACION = %s, TELEFONO = %s WHERE CODIGO = %s"
    valores = (name, telf, codigo)
    mycursor.execute(sql, valores)
    mydb.commit()
    while True:
        respuesta = input("¿Desea actualizar otra ubicación? Si responde no, será llevado de vuelta al menú de las ubicaciones (s/n): ")
        if respuesta.lower() == 's':
            actualizar_ubicacion()
            break
        elif respuesta.lower() == 'n':
            menu_ubicaciones()
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")    


def buscar_ubicacion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        codigo = input("Ingrese el código de la ubicación que desea buscar: ")
        sql_verif = ("SELECT * FROM ubicaciones WHERE CODIGO = %s")
        mycursor.execute(sql_verif, (codigo,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El lote ingresado no existe en la base de datos. Intente nuevamente.")
    print("\nInformación del medicamento:")
    print("Código:", resultado[0])
    print("Nombre de la ubicación:", resultado[1])
    print("Teléfono de la ubicación:", resultado[2])
    while True:
        respuesta = input("¿Desea buscar otra ubicación? Si responde no, será llevado de vuelta al menú de las ubicaciones (s/n): ")
        if respuesta.lower() == 's':
            buscar_ubicacion()
            break
        elif respuesta.lower() == 'n':
            menu_ubicaciones()
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.") 

def ver_ubicacion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ubicaciones")
    resultados = mycursor.fetchall()
    print("\nInformación de las Ubicaciones: ")
    for ubicacion in resultados:
        print("Código:", ubicacion[0])
        print("Nombre:", ubicacion[1])
        print("Telefono:", ubicacion[2])
        print("-------------------------")
    while True:
        respuesta = input("Presione 'r' para regresar al menú principal de ubicaciones: ")
        if respuesta.lower() == 'r':
            menu_ubicaciones()
            break
        else:
            print("Opción no válida. Por favor, ingrese 'r' para regresar al menú principal.")

def eliminar_ubicacion():
    mydb = mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database ="trabajofinaldb"
        )
    mycursor = mydb.cursor()
    while True:
        codigo = input("Ingrese el codigo de la ubicación que desea eliminar: ")
        sql_verif = ("SELECT * FROM ubicaciones WHERE CODIGO = %s")
        mycursor.execute(sql_verif, (codigo,))
        resultado = mycursor.fetchone()
        if resultado:
            break
        else:
            print("El codigo ingresado no existe en la base de datos. Intente nuevamente.")
    sql = "DELETE FROM ubicaciones WHERE CODIGO = %s"
    mycursor.execute(sql, (codigo,))    
    mydb.commit()
    print('Eliminado exitosamente.')
    while True:
        respuesta = input("¿Desea eliminar otra ubicación? Si responde no, será llevado de vuelta al menú de las ubicaciones (s/n): ")
        if respuesta.lower() == 's':
            eliminar_ubicacion()
            break
        elif respuesta.lower() == 'n':
            menu_ubicaciones()  
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")
            continue