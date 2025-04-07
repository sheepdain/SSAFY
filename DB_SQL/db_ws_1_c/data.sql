-- Active: 1744001268397@@127.0.0.1@3306
SELECT genre, count(*) as count FROM songs GROUP BY genre;

SELECT genre, count(*), avg(duration) as average_duration FROM songs  GROUP BY genre