from flask import Flask

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

import psycopg2
try:
    connection = psycopg2.connect(user = "iot",
                                  password = "iot1234",
                                  host = "ec2-3-80-128-28.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "iot")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
    cursor.execute("SELECT name station_masters")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

