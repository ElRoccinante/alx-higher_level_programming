-- creat database
create database if not exists hbtn_0d_usa;
use hbtn_0d_usa;
create table if not exists cities (
id INT not null PRIMARY KEY  AUTO_INCREMENT,
state_id INT not null ,
name VARCHAR(256) not null,
FOREIGN KEY (state_id) REFERENCES states(id)

);
