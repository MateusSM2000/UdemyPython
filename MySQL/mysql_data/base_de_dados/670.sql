select * from users as u, profiles as p;
select u.id, p.id from users as u, profiles as p;
select u.id, p.id from users as u, profiles as p where u.id = user_id;
select u.id, p.id, first_name, user_id, bio from users as u, profiles as p where u.id = user_id;
