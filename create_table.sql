CREATE TABLE rides(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    pickup_datetime DATETIME,
    dropoff_datetime DATETIME,
    trip_distance DECIMAL(5,2),
    pickup_longitude DECIMAL(10,7),
    pickup_latitude DECIMAL(10,7),
    dropoff_longitude DECIMAL(10,7),
    dropoff_latitude DECIMAL(10,7),
    total_amount DECIMAL(5,2),
    PRIMARY KEY(id)
);