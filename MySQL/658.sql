select * from users; -- seleciona colunas
select email from users;
select first_name from users;
select last_name, password_hash from users;
select last_name as ln, password_hash as ph from users;
select users.last_name from users;