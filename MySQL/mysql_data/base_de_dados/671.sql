select users.id as uid, profiles.id as pid, profiles.bio, users.first_name from users inner join profiles on users.id = profiles.user_id;
select users.id as uid, profiles.id as pid, profiles.bio, users.first_name from users inner join profiles on users.id = profiles.user_id where users.first_name like '%a'
order by users.first_name asc;