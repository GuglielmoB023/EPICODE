import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

user = 'root'
password = 'database23'
host = '127.0.0.1'
database = 'ecommerce'

def connection_database (user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except  mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None

def close_connection(connection):
    connection.close()

conn = connection_database(user, password, host, database)
cursor = conn.cursor()

db_connection_str = 'mysql+pymysql://root:database23@localhost/ecommerce'
db_connection = create_engine(db_connection_str)

def query(select, frm, join1=None, join2=None, join3=None, join4=None, where=None, groupby=None, orderby=None):
    stmt = 'select %s from %s ' % (select,frm)
    if join1 is not None:
        stmt = stmt + 'join %s ' % join1
    if join2 is not None:
        stmt = stmt + 'join %s ' % join2
    if join3 is not None:
        stmt = stmt + 'join %s ' % join3
    if join4 is not None:
        stmt = stmt + 'join %s ' % join4
    if where is not None:
        stmt = stmt + 'where %s ' % where
    if groupby is not None:
        stmt = stmt + 'group by %s ' % groupby
    if orderby is not None:
        stmt = stmt + 'order by %s' % orderby
    stmt = stmt + ';'
    return stmt

def dataframe (qsql):
    q = pd.read_sql(qsql,db_connection)
    return q

# 1. Articoli mancanti
select = 'nome'
frm = 'prodotto'
join1 = None
join2 = None
join3 = None
join4 = None
where = 'quantita = 0'
groupby = None
orderby = None

qsql1 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql1)
qpandas1 = dataframe(qsql1)
print('La prima query è \n', qsql1, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas1 )

# 2. Ordini che segnalano un problema
select = 'oid'
frm = 'ordine'
join1 = 'stato on ordine.stid = stato.stid '
join2 = None
join3 = None
join4 = None
where = 'stato.nome = \'problema\''
groupby = None
orderby = None

qsql2 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql2)
qpandas2 = dataframe(qsql2)
print('La seconda query è \n', qsql2, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas2)

# 3.Ordinamento discendente delle categorie di prodotti per quantità
select = 'categoria.nome'
frm = 'categoria'
join1 = 'prodotto on categoria.cid = prodotto.cid '
join2 = None
join3 = None
join4 = None
where = None
groupby = None
orderby = 'prodotto.quantita desc'

qsql3 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql3)
qpandas3 = dataframe(qsql3)
print('La terza query è \n', qsql3, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas3)

# 4. Ordinamento utenti in base a quanto hanno speso
select = 'distinct uid, nome, max(orpr01.prezzo * orpr01.quantita)'
frm = 'utente'
join1 = 'orpr01 on utente.lsid = orpr01.lsid'
join2 = None
join3 = None
join4 = None
where = None
groupby = 'uid, nome'
orderby = 'max(orpr01.prezzo * orpr01.quantita) desc'

qsql4 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
print(qsql4)
cursor.execute(qsql4)
qpandas4 = dataframe(qsql4)
print('La terza query è \n', qsql4, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas4)

# 5. Media di quanto hanno speso gli utenti
select = 'distinct uid, nome, avg(orpr01.prezzo * orpr01.quantita)'
frm = 'utente'
join1 = 'orpr01 on utente.lsid = orpr01.lsid'
join2 = None
join3 = None
join4 = None
where = None
groupby = 'uid, nome'
orderby = None

qsql5 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
print(qsql5)
cursor.execute(qsql5)
qpandas5 = dataframe(qsql5)
print('La terza query è \n', qsql5, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas5)

# 6. Riventitori di schede video
select = 'distinct utente.nome'
frm = 'utente'
join1 = 'listino on utente.lsid = listino.lsid'
join2 = 'orpr01 on listino.lsid = orpr01.lsid'
join3 = 'prodotto on orpr01.pid = prodotto.pid'
join4 = 'categoria on prodotto.cid = categoria.cid'
where = 'listino.nome = \'rivenditori\' and categoria.nome = \'SCHEDE VIDEO PCI-EXPRESS\''
groupby = None
orderby = None

qsql6 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql6)
qpandas6 = dataframe(qsql6)
print('La sesta query è \n', qsql6, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas6)


# 7. Numero ordini fatti dagli utenti
select = 'distinct utente.nome, count(utente.nome) as numero_ordini'
frm = 'utente'
join1 = 'ordine on utente.uid = ordine.uid'
join2 = None
join3 = None
join4 = None
where = None
groupby = 'nome'
orderby = None

qsql7 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql7)
qpandas7 = dataframe(qsql7)
print('La settimana query è \n', qsql7, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas7)


# 8. Nome utente e prodotti acquistati degli utenti standard
select = 'utente.nome, prodotto.nome as nome_prodotto, orpr01.quantita'
frm = 'utente'
join1 = 'listino on utente.lsid = listino.lsid'
join2 = 'orpr01 on listino.lsid = orpr01.lsid'
join3 = 'prodotto on orpr01.pid = prodotto.pid'
join4 = None
where = 'listino.nome = \'standard\''
groupby = None
orderby = None

qsql8 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql8)
qpandas8 = dataframe(qsql8)
print('L\'ottava query è \n', qsql8, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas8)

# 9. Utenti che hanno pagato in contrassegno
select = 'distinct utente.nome'
frm = 'utente'
join1 = 'ordine on utente.uid = ordine.uid'
join2 = 'pasp01 on ordine.paspid = pasp01.paspid'
join3 = 'pagamento on pasp01.paid = pagamento.paid'
join4 = None
where = 'pagamento.nome = \'contrassegno\''
groupby = None
orderby = None

qsql9 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql9)
qpandas9 = dataframe(qsql9)
print('La nona query è \n', qsql9, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas9)

# 10. Elenco prodotti acquistati per ordine decrescente
select = ' distinct prodotto.nome, orpr01.quantita '
frm = 'prodotto'
join1 = 'orpr01 on prodotto.pid = orpr01.pid'
join2 = None
join3 = None
join4 = None
where = None
groupby = None
orderby = 'orpr01.quantita desc'

qsql10 = query(select,frm,join1,join2,join3,join4,where,groupby,orderby)
cursor.execute(qsql10)
qpandas10 = dataframe(qsql10)
print('La decima query è \n', qsql10, '\nche restituisce in SQL:\n', cursor.fetchall(), '\ne in pandas:\n', qpandas10)

esc = close_connection(conn)