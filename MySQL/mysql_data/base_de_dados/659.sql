select * from users;
-- where filtra registros
select * from users where id = 2;
select * from users where first_name = 'Luiz';
-- operadores de comparaçào = < > >= <= <> !=
select * from users where id < 19;
select * from users where id <= 19;
select * from users where id != 19;
select * from users where id <> 19;
select * from users where created_at > '2025-06-20 17:04:57';
-- operadores lógicos and | or
select * from users where created_at > '2025-06-20 17:04:57' and first_name = 'Luiz';
select * from users where first_name = 'Luiz' or first_name = 'Mateus';