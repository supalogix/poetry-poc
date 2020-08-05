CREATE SCHEMA IF NOT EXISTS health_check;

CREATE TABLE IF NOT EXISTS health_check.random_message
(
    message TEXT
);

insert into health_check.random_message values ('hello world');