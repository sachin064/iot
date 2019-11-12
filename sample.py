import psycopg2


def get_records(query):
    connection = psycopg2.connect(user="iot",
                                  password="iot1234",
                                  host="ec2-3-80-128-28.compute-1.amazonaws.com",
                                  port="5432",
                                  database="iot"
                                  )

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    print(query)
    cursor.execute(query)
    record = cursor.fetchall()
    print("done")
    print("You are connected to - ", record, "\n")
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return record
