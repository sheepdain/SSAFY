-- Active: 1744075301631@@127.0.0.1@3306
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT NOT NULL,
  age INT NOT NULL
);

INSERT INTO zoo 
VALUES
('Lion', 'Meat', 200, 120, 5),
('Elephant', 'Plants', 5000, 300, 15),
('Giraffe', 'Leaves', 1500, 550, 10),
('Monkey', 'Fruits', 50, 60, 8);


SELECT * FROM zoo