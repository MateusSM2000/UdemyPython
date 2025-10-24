-- limit limita a busca
-- offset x desloca o valor inicial de um range em x unidades

select * from users;
select * from users where id between 50 and 100 order by first_name asc;
select * from users where id between 50 and 100 order by first_name asc limit 10;
select * from users where id between 50 and 100 order by first_name asc limit 5;
select * from users where id between 50 and 100 order by first_name asc limit 10 offset 0;
select * from users where id between 50 and 100 order by first_name asc limit 10 offset 6;
select * from users where id between 50 and 100 order by first_name asc limit 10 offset 11;
select * from users where id between 50 and 100 order by first_name asc limit 6,10; -- limit offset,limit