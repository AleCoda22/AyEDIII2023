import sqlite3

conexion=sqlite3.connect("bd1.db")
conexion.execute("insert into clientes(codigo,name,surname,phone) values (?,?)", (101,"Diego", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
conexion.commit()
conexion.close()