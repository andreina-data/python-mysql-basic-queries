import mysql.connector as db

#Conexión a la base de datos en mysql workbench
try:
    mydb = db.connect(
        host="localhost",
        user="root",
        passwd="mysql123",
        database="mp1"
    )
    my_cursor = mydb.cursor()
    print("Conectado exitosamente a la base de datos mp1.")

except db.Error as error:
    print("Error al conectar a la base de datos:", error)
    exit()

# Consultas: a. Información de la Sociedad con RUT 77886308-1

sqlSentence = "SELECT * FROM sociedades WHERE rut = '77886308-1'"
my_cursor.execute(sqlSentence)
results = my_cursor.fetchall()
for row in results:
    print(row)

# Consultas: b.  Sociedades cuyo nombre comience con la palabra “Agencia”

    sqlSentence = "SELECT * FROM sociedades"
    my_cursor.execute(sqlSentence)
    result = my_cursor.fetchall()
    print("\n Sociedades que comienzan con Agencia")
    filtered = []
    for x in result:
        if x[2].lower().startswith('agencia'):
            filtered.append(x)
print(filtered)

# Consultas: c.  Sociedades cuyo capital es mayor o igual a $400.000.000

sqlSentence = "SELECT * FROM sociedades WHERE capital >= 400000000"
my_cursor.execute(sqlSentence)
results = my_cursor.fetchall()
print("\n Sociedades con capital mayor o igual a $400.000.000:")
for row in results:
    print(row)

# Insertar una nueva sociedad a la tabla

sqlInsert = """
INSERT INTO sociedades (id, rut, nombre, registro, comuna, capital)
VALUES (%s, %s, %s, %s, %s, %s)
"""
valores = (
    5156305,
    '77721389-K',
    'Estrellas SpA',
    '2024-03-11',
    'PROVIDENCIA',
    1000000
)

# Manejo de errores
try:
    my_cursor.execute(sqlInsert, valores)
    mydb.commit()
    print("Sociedad 'Estrellas SpA' insertada correctamente.")
except db.Error as error:
    print("No se pudo insertar la sociedad:", error)

# Guardar cambios
mydb.commit()