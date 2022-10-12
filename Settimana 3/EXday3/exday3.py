import mysql.connector

user = 'root'
password = 'database23'
host = '127.0.0.1'
database = 'discografia'

def connection_database (user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except  mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None

conn = connection_database(user, password, host, database)
cursor = conn.cursor

select = 'NomeCantante'
frm = 'canzone'
join1 = 'esecuzione on canzone.CodiceReg=esecuzione.CodiceReg'
join2 = 'autore on esecuzione.TitoloCanzone=autore.TitoloCanzone'
where = 'nome=NomeCantante and nome like \'D%\''


def query(select, frm, join1=None, join2=None, where=None):
    stmt = 'select %s from %s ' % (select,frm)
    if join1 is not None:
        stmt = stmt + 'join %s ' % join1
    if join2 is not None:
        stmt = stmt + 'join %s ' % join2
    if where is not None:
        stmt = stmt + 'where %s ' % where
    stmt = stmt + ';'
    return stmt

esercizio1 = query(select,frm,join1,join2,where)
print(esercizio1)

select = 'TitoloAlbum'
frm = 'disco'
join1 = 'contiene on disco.NroSerie=contiene.NroSerieDisco'
join2 = 'esecuzione on contiene.CodiceReg=esecuzione.CodiceReg'
where = 'esecuzione.Anno is NULL'

esercizio2 = query(select,frm,join1,join2,where)
print(esercizio2)

select = 'distinct NomeCantante'
frm = 'canzone'
join1 = None
join2 = None
select2 = 'S1.NomeCantante'
frm2 = 'canzone as S1'
select3 = 'CodiceReg'
frm3 = 'canzone as S2'
where3 = 'S2.NomeCantante <> S1.NomeCantante))'
where2 = 'CodiceReg not in (' + query(select3,frm3,where3)
where = 'NomeCantante not in (' + query(select2,frm2,where2)

esercizio3 = query(select,frm,join1,join2,where)
print(esercizio3)

select = 'NomeCantante'
frm = 'cantante'
join1 = None
join2 = None
select2 = 'S1.NomeCantante'
frm2 = 'canzone as S1'
join3 = 'esecuzione on CodiceReg=S1.CodiceReg'
join4 = 'canzone as S2 on CodiceReg=S2.CodiceReg'
where2 = 'S1.NomeCantante <> S2.NomeCantante'
where = 'NomeCantante not in' + query(select2, frm2, join3, join4, where2)

esercizio4 = query(select,frm,join1,join2,where)
print(esercizio4)


insert = '' # 'autore'
list1 = []  # 'nome', 'TitoloCanzone'
list2 = []  # '\'Salmo\'', '\'Daytona\''

def inserimento(insert,list1,list2):
    stm = 'insert into %s' % (insert)
    stm = stm + '('
    for i in range(len(list1)):
        if i == len(list1)-1:
            stm = stm + list1[i]
        else:
            stm = stm + list1[i] + ', '
    stm = stm + ') values ('
    for k in range(len(list2)):
        if k == len(list2)-1:
            stm = stm + list2[k]
        else:
            stm = stm + list2[k] + ', '
    stm = stm + ')'
    return stm

inserimento1 = inserimento(insert,list1,list2)
print(inserimento1)

delete = ''
d_where = ''

def eliminazione(delete,d_where):
    stm = 'delete from %s ' % (delete)
    stm = stm + 'where %s ' % (d_where)
    return stm

eliminazione1 = eliminazione(delete,d_where)
print(eliminazione1)


def execute_query(cursor, stmt):
    try:
        cursor.execute(stmt)
        conn.commit()
    except:
        conn.rollback()

r1 = execute_query(cursor,esercizio1)
r2 = execute_query(cursor,esercizio2)
r3 = execute_query(cursor,esercizio3)
r4 = execute_query(cursor,esercizio4)
ins = execute_query(cursor,inserimento1)
canc = execute_query(cursor,eliminazione1)

result = cursor.fetchall()
print(result)

def close_connection(connection):
    connection.close()