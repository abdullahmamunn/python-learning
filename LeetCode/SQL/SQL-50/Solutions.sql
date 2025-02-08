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

10. 
