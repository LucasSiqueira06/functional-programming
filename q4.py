import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="lucas",
    password="123456789",
    database="UsuariosConsoles"
)

cursor = connection.cursor()

insert_record = lambda table, data: cursor.execute(
    f"INSERT INTO {table} ({', '.join(data.keys())}) VALUES ({', '.join(['%s'] * len(data))})",
    tuple(data.values())
)

delete_record = lambda table, condition: cursor.execute(
    f"DELETE FROM {table} WHERE {condition}"
)

get_records = lambda table, condition=None: (
    cursor.execute(f"SELECT * FROM {table}" + (f" WHERE {condition}" if condition else "")),
    cursor.fetchall()
)

insert_data = {
    "nome": "Lucas Siqueira",
    "console": "PS5"
}
insert_record("USUARIOS", insert_data)
connection.commit()

delete_record("USUARIOS", "id=1")
connection.commit()

records = get_records("JOGOS")[1]
print(records)

connection.close()