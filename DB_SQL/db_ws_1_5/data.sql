-- Active: 1744006994910@@127.0.0.1@3306
SELECT * FROM users WHERE age>=30 AND balance>=1000;

SELECT * FROM users WHERE balance<=1000 and age<=20;

SELECT * FROM users WHERE first_name LIKE '현%' and country='제주특별자치도' ORDER BY age DESC LIMIT 1;

SELECT * FROM users WHERE last_name='박' and age>=25 ORDER BY age LIMIT 1;

SELECT * FROM users WHERE first_name='재은' or first_name='영일' ORDER BY balance DESC LIMIT 1;

SELECT * FROM users GROUP BY country HAVING max(balance) ORDER BY balance DESC;

SELECT * FROM users WHERE age>= 30 AND balance>(SELECT avg(balance) FROM users WHERE age>=30);