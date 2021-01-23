SELECT 
    MAX(Salary) AS Salary
FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees)