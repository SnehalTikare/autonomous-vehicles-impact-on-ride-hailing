import mysql.connector
import pandas as pd

def insert_rows():
    for index, row in rides.iterrows():
        pickup_datetime = row["tpep_pickup_datetime"]
        dropoff_datetime = row["tpep_dropoff_datetime"]
        trip_distance = round(row["trip_distance"], 2)
        pickup_longitude = round(row["pickup_longitude"], 7)
        pickup_latitude = round(row["pickup_latitude"], 7)
        dropoff_longitude = round(row["dropoff_longitude"], 7)
        dropoff_latitude = round(row["dropoff_latitude"], 7)
        total_amount = round(row["total_amount"], 2)

        stmt = '''
        INSERT INTO rides
        (pickup_datetime, dropoff_datetime, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, total_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        insert_tuple = (
            pickup_datetime,
            dropoff_datetime,
            trip_distance,
            pickup_longitude,
            pickup_latitude,
            dropoff_longitude,
            dropoff_latitude,
            total_amount
        )

        # Insert into DB
        CURSOR.execute(stmt, insert_tuple)

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="av_impact",
    auth_plugin='mysql_native_password'
)
CURSOR = DB.cursor(prepared=True)

rides = pd.read_csv("yellow_tripdata_2015-01.csv")

def main():

    # Do all your pre - processing before calling insert rows
    insert_rows()
    # Uncomment the below line only when you're ready to commit to the DB. Till then none of the
    # changes will be reflected in the DB
    # Run it only once. Since none of the entries are unique there's no way to check if a ride
    # already exists in the DB so it will insert twice
    DB.commit()

if __name__ == "__main__":
    main()
