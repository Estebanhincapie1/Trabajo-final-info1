import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="informatica1",
  password="bio123",
  database ="trabajofinaldb"
)

mycursor = mydb.cursor()

# Aquí creé la base de datos, va comentada porque si corremos el código va a crear otra con este mismo nombre
#mycursor.execute("CREATE DATABASE trabajofinaldb")

# mycursor = mydb.cursor()
# # Aquí creé la tabla que contiene los usuarios (username va con UNIQUE para que no hayan valores repetidos en esta columna), va comentada porque cuando se corra el código va a intentar crear otra tabla con esa información
# mycursor.execute("CREATE TABLE usuarios (username VARCHAR(255) UNIQUE, password VARCHAR(255))")

# mycursor = mydb.cursor()
# #Aquí agregué los credenciales a la tabla de usuarios, después utilizamos mydb.commit() para que se guarden los cambios realizados. Va comentada para que no se haga dos veces.
# mycursor.execute("INSERT INTO usuarios (username, password) VALUES ('juanes', '123juanes')")
# mydb.commit()

# # Esto es para imprimir la info de la tabla y confirmar que entraron los caracteres
# mycursor.execute("SELECT username, password FROM usuarios")
# result = mycursor.fetchall()

# for row in result:
#     print(row)

#Aquí creé la tabla que contiene los medicamentos. 
# mycursor.execute("CREATE TABLE medicamentos (LOTE VARCHAR(255), NOMBRE VARCHAR(255), DISTRIBUIDOR VARCHAR(255), CANTIDAD VARCHAR(255), LLEGADA VARCHAR(255), PRECIOVENTA VARCHAR(255))")

#Aquí creé la tabla de los proveedores.
# mycursor.execute("CREATE TABLE proveedores (CODIGO VARCHAR(255), NOMBRE VARCHAR(255), APELLIDO VARCHAR(255), ID VARCHAR(255), ENTIDAD VARCHAR(255))")

#Aquí creé la tabla de las ubicaciones
# mycursor.execute("CREATE TABLE ubicaciones (CODIGO VARCHAR(255), NOMBREUBICACION VARCHAR(255), TELEFONO VARCHAR(255))")

#alimentamos la tabla de medicmanentos con una lista
# medicamentos = [("1234", "alizaprida", "coomedic", "11758", "21-05-2023", "54500"),
#                 ("7895a", "doxiciclina", "infraneur", "7896", "16-05-2023", "27500"),
#                 ("5289cd", "clembuterol", "labsys", "2596", "11-05-2023", "1356")]

# sql = "INSERT INTO medicamentos (LOTE, NOMBRE, DISTRIBUIDOR, CANTIDAD, LLEGADA, PRECIOVENTA) VALUES (%s, %s, %s, %s, %s, %s)"
# mycursor.executemany(sql, medicamentos)
# mydb.commit()

#confirmamos que la información se ingresó correctamente
# sql = "SELECT * FROM medicamentos"
# mycursor.execute(sql)
# resultados=mycursor.fetchall()
# for i in resultados:
#     print(i)

#alimentamos la tabla de proveedores con una lista
# proveedores = [("1234z", "Juan", "Perez", "1122334455", "coomedic"),
#                 ("7895as", "Andres", "Molina", "1221324354", "infraneur"),
#                 ("5289cds", "Sergio", "Olejua", "9090526", "labsys")]
# sql = "INSERT INTO proveedores (CODIGO, NOMBRE, APELLIDO, ID, ENTIDAD) VALUES (%s, %s, %s, %s, %s)"
# mycursor.executemany(sql, proveedores)
# mydb.commit()

#confirmamos que la información se ingresó correctamente
# sql = "SELECT * FROM proveedores"
# mycursor.execute(sql)
# resultados=mycursor.fetchall()
# for i in resultados:
#     print(i)

#alimentamos la tabla de ubicaciones con una lista
# ubicaciones  = [("254axc03", "SanVicente", "0345742177"),
#                 ("7889j45l", "LeonXIII", "0342153385"),
#                 ("1250powr", "Cardioinfantil", "0348496635")]
# sql = "INSERT INTO ubicaciones (CODIGO, NOMBREUBICACION, TELEFONO) VALUES (%s, %s, %s)"
# mycursor.executemany(sql, ubicaciones)
# mydb.commit()

#confirmamos que la información se ingresó correctamente
# sql = "SELECT * FROM ubicaciones"
# mycursor.execute(sql)
# resultados=mycursor.fetchall()
# for i in resultados:
#     print(i)

from funciones import *

validar_usuario()