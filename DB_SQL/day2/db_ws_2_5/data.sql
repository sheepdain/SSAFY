-- Active: 1744082168431@@127.0.0.1@3306
INSERT INTO employees (id, name, salary, age, departmentId) VALUES
  (9, '이규보', 1700, 77, 1), 
  (10, '김구', 126000, 21, 2),
  (11,'유관순',82000, 41, 4),
  (12, '개발자', 23000, 37,3);

SELECT d.name AS department, e.name AS oldest_employee, e.age AS max_age, avg(e.age) as avg_age FROM employees e
JOIN departments d ON e."departmentId"=d.id
GROUP BY d.id
HAVING e.age=max(age)
ORDER BY department

SELECT d.name AS department, e.name AS highest_paid_employee, e.salary AS max_salary FROM employees e
JOIN departments d ON e."departmentId"=d.id
GROUP BY d.id
HAVING e.salary=max(e.salary)

SELECT d.name AS department,
CASE 
  WHEN e.age BETWEEN 30 AND 40 THEN 'BETWEEN 30-40'
  WHEN e.age > 40 THEN 'OVER 40'
  WHEN e.age < 30 THEN 'UNDER 30'
END AS age_group,
count(*) 
FROM employees e
JOIN departments d ON e."departmentId"=d.id
GROUP BY d.id, age_group
ORDER BY department

SELECT d.name AS department,avg(e.salary) as avg_salary_excluding_highest FROM employees e
JOIN departments d  on e."departmentId"=d.id
WHERE e.salary<(SELECT max(sube.salary) FROM employees sube WHERE sube."departmentId"=e."departmentId")
GROUP BY d.id
ORDER BY department
