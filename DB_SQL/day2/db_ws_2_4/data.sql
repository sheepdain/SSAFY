-- Active: 1744086268604@@127.0.0.1@3306
CREATE Table transactions(
  id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL,
  amount TEXT NOT NULL,
  transaction_date DATE NOT NULL,
  Foreign Key (user_id) REFERENCES users(id)
);

INSERT INTO transactions(user_id,amount,transaction_date) VALUES
(1,'500','2024-03-15'),
(2,'700','2024-03-16'),
(1,'200','2024-03-17'),
(3,'1000','2024-03-18');

SELECT users.first_name, users.last_name, transactions.amount, transactions.transaction_date FROM users
JOIN transactions ON users.id=transactions.user_id;

SELECT users.first_name, users.last_name, transactions.amount, transactions.transaction_date FROM users
JOIN transactions ON users.id=transactions.user_id
WHERE transactions.transaction_date>'2024-03-16';

SELECT users.first_name, users.last_name, sum(transactions.amount) as total_amount FROM users
JOIN transactions ON users.id=transactions.user_id
GROUP BY users.id

