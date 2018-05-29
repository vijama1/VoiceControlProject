# VoiceControlProject
ML Project - Voice Controlled Computer Operations

Install PyMySQL
sudo apt-get install python3-pymysql

Creating database in pymysql:
mysql>create database speech_recognition;
mysql>use speech_recognition;

Creating a table in pymysql:
mysql>create table commands
      (user_input varchar(50),
       command varchar(30));

Loading data into table:
mysql>load data local infile '<path to csv file>' into table commands columns terminated by ',';
