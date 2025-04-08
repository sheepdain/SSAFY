-- Active: 1744075468001@@127.0.0.1@3306
ALTER TABLE zoo
ADD COLUMN 'species' TEXT NOT NULL DEFAULT 'sub';

SELECT * FROM zoo;

UPDATE zoo
SET 
height=height*2.54,
species='Panthera leo'
WHERE name='Lion';

UPDATE zoo
SET 
height=height*2.54,
species='Loxodonta africana'
WHERE name ='Elephant';

UPDATE zoo
SET 
height=height*2.54,
species='Giraffa camelopardalis'
WHERE name ='Giraffe';

UPDATE zoo
SET 
height=height*2.54,
species='Cebus capucinus'
WHERE name ='Monkey';

SELECT * FROM zoo;