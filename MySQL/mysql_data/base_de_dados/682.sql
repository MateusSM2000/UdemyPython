select
max(salary) as max_salary,
min(salary) as min_salary,
avg(salary) as avg_salary,
sum(salary) as sum_salary,
count(salary) as contagem
from users;

select
max(salary) as max_salary,
min(salary) as min_salary,
avg(salary) as avg_salary,
sum(salary) as sum_salary,
count(salary) as contagem
from users
where first_name = 'Luiz';

select
first_name,
max(salary) as max_salary,
min(salary) as min_salary,
avg(salary) as avg_salary,
sum(salary) as sum_salary,
count(salary) as contagem
from users
group by first_name;