
import snowflake.connector as sf
from config import config

conn = sf.connect(user=config.usename,password=config.password,account=config.account)

def execute_query(connection, query):
    cursor= connection.cursor()
    cursor.execute(query)
    cursor.close()


try:
    sql='use {}'.format(config.database)
    execute_query(conn,sql)

    sql='use warehouse {}'.format(config.warehouse)
    execute_query(conn, sql)

    try:
        sql='alter warehouse {} resume'.format(config.warehouse)
        execute_query(conn, sql)
    except:
        pass

    sql="select * from TEST"
    cursor=conn.cursor()
    cursor.execute(sql)
    for c in cursor:
        print(c)

except Exception as e:
    print(e)