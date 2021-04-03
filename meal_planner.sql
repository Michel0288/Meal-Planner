DROP DATABASE IF EXISTS meal_planner;
CREATE DATABASE meal_planner;
USE meal_planner;

DROP TABLE IF EXISTS account;
CREATE TABLE account(
    account_id INT NOT NULL unique AUTO_INCREMENT ,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR (6) NOT NULL,
    height INT NOT NULL,
    weight INT NOT NULL,
    allergies VARCHAR (50),
    dietarylifestyle VARCHAR(50), 
    dietaryrestrictions VARCHAR(50),
    goal VARCHAR(50),
    dailycalories INT,
    photo VARCHAR(200),
    PRIMARY KEY(account_id)
);
