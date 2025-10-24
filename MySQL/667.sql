select 1 as coluna, 'qualquer coisa' as col2;
insert into profiles (bio, user_id) select concat('Bio de ', first_name), id from users;
delete from profiles;