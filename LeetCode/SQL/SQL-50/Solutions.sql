# Write your MySQL query statement below
Answers

1. select product_id from Products where low_fats = 'Y' and recyclable = 'Y'; 
2. select name from Customer where referee_id != 2 or referee_id is null;
3. select name, population, area from World where area >= 3000000 or population >= 25000000;
4. select distinct(author_id) as id from Views where author_id = viewer_id order by author_id asc
5. select tweet_id from Tweets where length(content) > 15;
6. select EmployeeUNI.unique_id, Employees.name from Employees left join EmployeeUNI on Employees.id = EmployeeUNI.id
7. select Product.product_name, Sales.year, Sales.price from Product join Sales on Product.product_id = Sales.product_id
8. select Visits.customer_id, count(Visits.visit_id) as count_no_trans from Visits left join Transactions on Visits.visit_id = Transactions.visit_id where Transactions.visit_id is null
   group by Visits.customer_id
9. SELECT w1.id
  FROM Weather w1
  JOIN Weather w2
  ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
  where w1.temperature > w2.temperature

10. SELECT 
    a1.machine_id, round(avg(a2.timestamp - a1.timestamp), 3) as processing_time  
    FROM Activity a1
    Join Activity a2
    ON a1.machine_id = a2.machine_id 
    AND a1.process_id = a2.process_id
    AND a1.activity_type = 'start'
    AND a2.activity_type = 'end'

    Group by a1.machine_id

11. select name, bonus
    from Employee e
    left join Bonus b
    on e.empId = b.empId
    where b.bonus < 1000 or b.bonus is null

12. # Write your MySQL query statement below
select s.student_id, student_name, sb.subject_name, count(e.subject_name) as attended_exams 
from Students s
join Subjects sb
left join Examinations e
on s.student_id = e.student_id and sb.subject_name = e.subject_name

group by s.student_id, sb.subject_name
order by s.student_id
13. select e2.name 
from Employee e1
join Employee e2
on e1.managerId = e2.id

group by e2.id
having count(*) >=5

14. SELECT
    s.user_id,
    ifnull(round(avg(action='confirmed'),2), 0) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id

15. select id,movie,description,rating 
from Cinema
where id%2=1 and description !='boring'
order by rating desc

16. # Write your MySQL query statement below
select p.product_id,
ifnull(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price
from Prices p
left join UnitsSold u
on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
group by product_id

17. 
select p.project_id, round(avg(e.experience_years), 2) as average_years
from Project p
left join Employee e
on p.employee_id  = e.employee_id
group by p.project_id

18. select r.contest_id,
       round(count(r.user_id) / (select count(*) from Users) * 100, 2) as percentage
from Register r
group by r.contest_id
order by percentage desc, r.contest_id asc

19. 
select query_name,
round(avg(rating/position), 2) as quality,
round(avg(rating <3)*100, 2) as poor_query_percentage
from Queries 

group by query_name

20.
select  
    DATE_FORMAT(trans_date , '%Y-%m') AS month, 
    t.country as country, 
    count(*) as trans_count, 
    sum(case when state = 'approved' then 1 else 0 end) as approved_count,
    sum(amount) as trans_total_amount, 
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions T
group by month, t.country;

or 
# Write your MySQL query statement below
select DATE_FORMAT(trans_date, "%Y-%m") as month,
country, count(trans_date) as trans_count,
sum(if(state = 'approved',1,0)) as approved_count,
sum(amount) as trans_total_amount,
sum(if(state = 'approved', amount, 0)) as approved_total_amount
from  Transactions
group by month, country




21.
22.
23.select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id



-- Find the second heighest salary, if no salary then null
-- soulution with order by and limit
select ifnull(
   (select distinct salary 
from Employee
order by salary desc
limit 1 offset 1), null) as SecondHighestSalary

-- solution with subquery
select max(salary) as SecondHighestSalary
from Employee
where salary < (select max(salary) from Employee)

-- Explanation: subquery will return the highest salary and then we will find the max salary which is less than the highest salary

-- Rank the employees based on their salary
selct e.emp_id, e.name, e.dept, e.salary,
rank() over (order by e.salary desc) as rank
from Employee e

-- Explanation: rank() function will rank the employees based on their salary in descending order

-- Find the nth highest salary
select ifnull(
   (select distinct salary
from Employee
order by salary desc
limit 1 offset n-1), null) as NthHighestSalary

-- Explanation: subquery will return the nth highest salary and then we will find the max salary which is less than the nth highest salary

-- Filter the customer with no order
select c.name as Customers
from Customers c
left join Orders o
on c.id = o.customerId
where o.customerId is null

-- Explanation: left join will return all the customers and orders, then we will filter the customers with no orders

-- find the customer with the highest order
select c.name as Customers
from Customers c
join Orders o
on c.id = o.customerId
group by c.name
order by sum(o.amount) desc

-- Explanation: join will return all the customers and orders, then we will group by customers and order by the sum of the amount in descending order

-- find duplicate emails
select email
from Person
group by email
having count(email) > 1

-- Explanation: group by email will group the emails and having count(email) > 1 will filter the duplicate emails

-- find the highest paid employee in each department 
-- make table schema and values for relavent tables

-- create
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);


-- insert
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'HR');

INSERT INTO employees (employee_id, name, salary, department_id) VALUES
(1, 'Alice', 80000, 1),
(2, 'Bob', 75000, 1),
(3, 'Charlie', 70000, 1),
(4, 'David', 65000, 2),
(5, 'Emma', 72000, 2),
(6, 'Frank', 60000, 3),
(7, 'Grace', 58000, 3);

-- fetch Find the highest-paid employee(s) in each department.
select e.employee_id, e.name, e.salary, d.department_name as department
from employees e
left join departments d 
on e.department_id = d.department_id

where e.salary = (select max(salary) from employees where department_id = d.department_id)

--Employees salary with rank
select e.employee_id, e.name, e.salary, d.department_name as department, RANK() over(order by e.salary DESC) as `rank`
from employees e
left join departments d 
on e.department_id = d.department_id

