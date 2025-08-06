-- asc é crescente
-- desc é decrescente

select * from users;
select id, first_name, email from users where id between 20 and 50 order by first_name asc;
select id, first_name, email from users where id between 20 and 50 order by created_at desc;
select id, first_name, email from users where id between 20 and 50 order by first_name asc, email desc;