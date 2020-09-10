import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=JACOB-PC;'
                      'Database=test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
# cursor.execute('SELECT * FROM people')
#cursor.execute('''
#create table test(
#id integer identity(1,1) primary key,
#uname text,
#score integer
#);
#''')
#conn.commit()


# for row in cursor:
# print(row)


def update(table, column, value, rid):
    cursor.execute("update %s set %d where %s = %d" % (table, value, column, rid))
    conn.commit()

def insert(table, uname, value):
    cursor.execute("insert into %s (uname, score) values (\'%s\', %d)" % (table, uname, value))
    conn.commit()

def delete(table, rid):
    cursor.execute("delete from %s where id = %d" % (table, rid))
    conn.commit()
