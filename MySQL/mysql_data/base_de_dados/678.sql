select u.id as uid, u.first_name, p.bio, ur.role_id, r.name as role
from users as u left join profiles as p on u.id = p.user_id
inner join users_roles as ur on u.id = ur.user_id
inner join roles as r on r.id = ur.role_id
order by u.id;