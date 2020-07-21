# demp
Project: Data Modeling with Postgres



Sparkify is a start-up business that owns music streaming app. To improve their performance they want to analyze the data that they have been collecting on songs and 
user activity to attain users preference in songs. Due to the uneasiness of the querying the data,it occupies in a directory of JSON logs on user activity on the
Sparkify app, along with a directory with JSON metadata on the songs in Sparkify app.


The goal of this project is to create a Postgres database by designing optimizing queries on song play and using ETL pipeline to analyze the data.


In this project, the star schema is used where the fact table is songplays and the four dimension tables are songs, artisits, users and times. 
The fact table is joined by only a single join with the dimension tables.
