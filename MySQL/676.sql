insert into users_roles (user_id, role_id)
select id, (select id from roles order by rand() limit 1) from users;