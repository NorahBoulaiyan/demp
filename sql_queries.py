# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs "
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
(songplay_id serial NOT NULL primary key, 
start_time timestamptz NOT NULL, 
user_id int NOT NULL, 
level varchar NOT NULL,
song_id varchar,
artist_id varchar, 
session_id int NOT NULL, 
location varchar, 
user_agent varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
(user_id int NOT NULL primary key, 
first_name varchar NOT NULL, 
last_name varchar NOT NULL, 
gender varchar, 
level varchar NOT NULL);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
(song_id varchar NOT NULL primary key, 
title varchar NOT NULL, 
artist_id varchar NOT NULL,
year int, 
duration float NOT NULL);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
(artist_id varchar NOT NULL primary key, 
name varchar NOT NULL, 
location varchar, 
latitude float, 
longitude float);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
(start_time timestamptz NOT NULL primary key, 
hour int NOT NULL, 
day int NOT NULL, 
week int NOT NULL, 
month int NOT NULL,
year int NOT NULL,
weekday int NOT NULL);
""")



songplay_table_insert =("""
INSERT INTO songplays(songplay_id,start_time,user_id, level, song_id,artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert =("""
INSERT INTO users(user_id,first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO UPDATE SET level=excluded.level;
""")

song_table_insert =("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id,name,location,latitude,longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT(artist_id) DO UPDATE SET name=artists.name, location=artists.location,  latitude=artists.latitude,longitude=artists.longitude;
""")

time_table_insert =("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO UPDATE SET hour=time.hour,day=time.day,week=time.week,month=time.month;
""")


# FIND SONGS
song_select = ("""
SELECT songs.song_id, artists.artist_id
    FROM songs
    JOIN artists ON artists.artist_id = songs.artist_id
    WHERE   songs.title = %s
    AND     songs.artist_id = %s
    AND     songs.duration = %s
    """)
    
# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
