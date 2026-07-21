CREATE TABLE departments (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    department_id INTEGER NOT NULL,
    CONSTRAINT fk_employees_departments
        FOREIGN KEY (department_id)
        REFERENCES departments(id)
);

INSERT INTO departments (name, location) VALUES
    ('IT', 'New York'),
    ('Marketing', 'Los Angeles'),
    ('Finance', 'New York'),
    ('HR', 'Chicago'),
    ('Operations', 'Los Angeles');

INSERT INTO employees (name, salary, department_id) VALUES
    ('John Smith', 75000, 1),
    ('Anna Johnson', 68000, 1),
    ('Michael Brown', 52000, 2),
    ('Emily Davis', 58000, 2),
    ('David Wilson', 82000, 3),
    ('Sophia Martinez', 61000, 3),
    ('James Taylor', 47000, 4),
    ('Olivia Anderson', 70000, 5);

-- 1. Employees whose salary is greater than the average salary.
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

-- 2. Every employee's name, salary, and department name without JOIN.
SELECT
    e.name,
    e.salary,
    (
        SELECT d.name
        FROM departments d
        WHERE d.id = e.department_id
    ) AS department_name
FROM employees e;

-- 3. Employees who work in departments located in New York.
SELECT name, salary
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'New York'
);

-- 4. Departments where at least one employee works.
SELECT name, location
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.id
);

-- 5. Employees who earn more than any employee in Marketing, using ANY.
SELECT name, salary
FROM employees
WHERE salary > ANY (
    SELECT e.salary
    FROM employees e
    WHERE e.department_id = (
        SELECT d.id
        FROM departments d
        WHERE d.name = 'Marketing'
    )
);

-- 6. Employees who earn more than all employees in IT, using ALL.
SELECT name, salary
FROM employees
WHERE salary > ALL (
    SELECT e.salary
    FROM employees e
    WHERE e.department_id = (
        SELECT d.id
        FROM departments d
        WHERE d.name = 'IT'
    )
);

-- 7. Employees from New York or Los Angeles, without duplicates.
SELECT e.name, e.salary
FROM employees e
WHERE e.department_id IN (
    SELECT d.id
    FROM departments d
    WHERE d.location = 'New York'
)
UNION
SELECT e.name, e.salary
FROM employees e
WHERE e.department_id IN (
    SELECT d.id
    FROM departments d
    WHERE d.location = 'Los Angeles'
);

-- 8. Same query with UNION ALL, including duplicates.
SELECT e.name, e.salary
FROM employees e
WHERE e.department_id IN (
    SELECT d.id
    FROM departments d
    WHERE d.location = 'New York'
)
UNION ALL
SELECT e.name, e.salary
FROM employees e
WHERE e.department_id IN (
    SELECT d.id
    FROM departments d
    WHERE d.location = 'Los Angeles'
);
