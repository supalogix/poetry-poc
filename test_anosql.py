import anosql
import psycopg2
import os

"""
    Make sure to export the environment variables for the database. 
    
    For example, you could use the following on a linux environment

    > export psycopg2_database=dba
    > export psycopg2_host=localhost
    > export psycopg2_password=mysecretpassword
    > export psycopg2_user=user
"""

def get_connection():
    host = os.environ.get("psycopg2_host")
    database = os.environ.get("psycopg2_database")
    user = os.environ.get("psycopg2_user")
    password = os.environ.get("psycopg2_password")

    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password)
    
    return conn

def get_query(config_path):
    query = anosql.from_path(config_path, 'psycopg2')
    
    return query

def get_random_messages():
    conn = get_connection()
    query = get_query("db/get_random_messages.pgsql")
    result = query.get_random_messages(conn)

    return result[0][0]

result = get_random_messages()
print(result)

assert(result == {'message': 'hello world'})