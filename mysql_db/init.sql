create database grades;
use grades;

create table grades (
    grade_id int NOT NULL AUTO_INCREMENT,
    user_id varchar(50) NOT NULL,
    course1 int not null,
    course2 int,
    course3 iNT,
    course4 int,
    course5 int,
    primary key (grade_id)
);

Insert into grades values
(NULL,'Steven',90,80,70,60,50);