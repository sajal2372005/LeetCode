SELECT 
    dep.name AS Department,
    emp1.name AS Employee,
    emp1.salary AS Salary
FROM 
    Employee emp1
JOIN 
    Department dep ON emp1.departmentId = dep.id
WHERE 
    3 > (
        SELECT COUNT(DISTINCT emp2.salary)
        FROM Employee emp2
        WHERE emp2.departmentId = emp1.departmentId 
        AND emp2.salary > emp1.salary
    );