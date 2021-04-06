DROP DATABASE IF EXISTS mealplanner;
CREATE DATABASE mealplanner;
USE mealplanner;

DROP TABLE IF EXISTS account;
CREATE TABLE account(
    account_id INT NOT NULL unique AUTO_INCREMENT ,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR (6) NOT NULL,
    height VARCHAR(15),
    weight INT NOT NULL,
    allergies VARCHAR (50),
    dietarylifestyle VARCHAR(50), 
    goal VARCHAR(50),
    photo VARCHAR(200),
    PRIMARY KEY(account_id)
);

DROP TABLE IF EXISTS recipe;
CREATE TABLE recipe(
    recipe_id INT NOT NULL unique AUTO_INCREMENT,
    recipe_name VARCHAR(200),
    preparation_time VARCHAR(150),
    meal_type VARCHAR(50),
    servings INT,
    photo VARCHAR(200),
    totalcalories INT,
    dateadded DATE DEFAULT NOW(),
    PRIMARY KEY(recipe_id)
);

DROP TABLE IF EXISTS ingredients;
CREATE TABLE ingredients(
    ingredient_id INT NOT NULL unique AUTO_INCREMENT,
    ingredient_name VARCHAR(200),
    calories_count INT,
    measurement VARCHAR(5000),
    recipe_id INT NOT NULL,
    PRIMARY KEY(ingredient_id),
    foreign key(recipe_id) references recipe(recipe_id) 
);

DROP TABLE IF EXISTS instructions;
CREATE TABLE instructions(
    instruction_id INT NOT NULL unique AUTO_INCREMENT,
    step_no INT,
    instruction VARCHAR(5000),
    recipe_id INT NOT NULL,
    PRIMARY KEY(instruction_id),
    foreign key(recipe_id) references recipe(recipe_id) 
);
/* SELECT stock_name FROM kitchen_stock JOIN ingredients ON stock_name=ingredient_name;

SELECT ingredient_name FROM ingredients JOIN recipe on ingredients.recipe_id=recipe.recipe_id JOIN meal_plan on meal_plan.recipe_id = recipe.recipe_id WHERE ingredient_name NOT IN (SELECT stock_name FROM kitchen_stock;); */
DROP TABLE IF EXISTS kitchen_stock;
CREATE TABLE kitchen_stock(
    stock_id INT NOT NULL unique AUTO_INCREMENT,
    mealplan_id INT NOT NULL,
    stock_name VARCHAR(200),
    quantity INT,
    PRIMARY KEY(stock_id),
    FOREIGN KEY(mealplan_id) REFERENCES meal_plan(mealplan_id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS meal_plan;
CREATE TABLE meal_plan(
    mealplan_id INT NOT NULL unique AUTO_INCREMENT,
    meal_week DATE,
    recipe_id INT NOT NULL,
    account_id INT NOT NULL,
    foreign key(recipe_id) references recipe(recipe_id) ON DELETE CASCADE ON UPDATE CASCADE,
    foreign key(account_id) references account(account_id) 
);

DELIMITER //
CREATE PROCEDURE SearchFilter(IN searchitem VARCHAR(100))
BEGIN
SELECT * FROM recipe WHERE recipe_name like %searchitem% OR totalcalories <= searchitem;
END //
DELIMITER ;

/*
PROCEDURE FOR SUPERMARKET LIST (DELETE THIS LINE AND UNCOMMENT PROCEDURE)
DELIMITER //
CREATE PROCEDURE supermarketlist
BEGIN
SELECT ingredient_name FROM recipe JOIN meal_plan on meal_plan.recipe_id = recipe.recipe_id WHERE ingredient_name NOT IN (SELECT ingredient_name FROM kitchen_stock;);
END //
DELIMITER ;
*/

/* 
DROP TABLE IF EXISTS meal;
CREATE TABLE meal(
    meal_id INT NOT NULL unique AUTO_INCREMENT,
    recipe_id INT NOT NULL,
    totalcalories INT NOT NULL,
    foreign key(recipe_id) references recipe(recipe_id)
); */
/*

    meal_id
    recipe_id INT NOT NULL unique AUTO_INCREMENT,
    recipe_name VARCHAR(200),
    meal_type VARCHAR(50),
    servings INT,
    photo VARCHAR(200),
    totalcalories
    PRIMARY KEY(recipe_id)

    Make a procedure with a view table

    create procedure for supermarket list


*/