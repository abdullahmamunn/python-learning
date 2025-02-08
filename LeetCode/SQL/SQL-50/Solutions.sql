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


