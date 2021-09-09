import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()

# result = select("nome, cpf, endereco", "alunos")
# print(result[3])

def insert(values, table, fields=None):

    global c, con

    query = "INSERT INTO " + table
    if(fields):
        query += " (" + fields + ") "
    query += " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()

values = [
    "DEFAULT, 'João Pedro', '2000-01-01', 'Av. das Pedras, 123', 'Betim', 'MG', '74635281017'",
    "DEFAULT, 'Maria Pedro', '2000-01-01', 'Av. das Pedras, 123', 'Betim', 'MG', '74635281018'"
]

# insert(values, "alunos")
# print(select("*", "alunos"))

def update(sets, table, where=None):

    global c, con

    query = "UPDATE " + table
    query += " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if(where):
        query += " WHERE " + where

    c.execute(query)
    con.commit()


# update({"nome":"João Martins", "cidade":"Curitiba"}, "alunos", "id_aluno = 13")
# print(select("*", "alunos", "id_aluno = 13"))

def delete(table, where):

    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()

# print(select("*", "alunos", "id_aluno = 13"))
# print(delete("alunos", "id_aluno = 13"))
# print(select("*", "alunos", "id_aluno = 13"))