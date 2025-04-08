-- Active: 1744069753867@@127.0.0.1@3306
SELECT * FROM artists;

SELECT count(*) FROM artists;

SELECT * FROM artists WHERE "Name"='AC/DC';

SELECT artistid, Name FROM artists;

SELECT * FROM artists WHERE "Name"='Gilberto Gil' OR "Name"='Ed Motta';

SELECT * FROM artists ORDER BY "Name" DESC;

SELECT * FROM artists WHERE "Name" LIKE 'Vinícius%' LIMIT 2;

SELECT Artistid FROM artists WHERE "ArtistId" BETWEEN 50 AND 70;