select first_name, count(id) as qtd from users
group by first_name
order by qtd desc;