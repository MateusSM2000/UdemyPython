-- % qql conjunto de caracteres
-- _ qql um caractere
select * from users;
select * from users where first_name like '%a';
select * from users where first_name like '%s';
select * from users where first_name like 'h%';
select * from users where first_name like 'ha%';
select * from users where first_name like 'ma%us';
select * from users where first_name like '%mo%';
select * from users where first_name like '%ol%';
select * from users where first_name like '%a%b%';
select * from users where first_name like '__c_b';
select * from users where first_name like '_____';