-- Active: 1744004204470@@127.0.0.1@3306
SELECT * FROM tracks WHERE Name LIKE '%love%';

SELECT * FROM tracks WHERE GenreId=1 and Milliseconds>=300000 ORDER BY UnitPrice DESC

SELECT GenreId, count(*) AS TotalTracks FROM tracks GROUP BY GenreId;

SELECT GenreId, sum("UnitPrice") AS TotalPrice FROM tracks GROUP BY GenreId HAVING TotalPrice>=100;