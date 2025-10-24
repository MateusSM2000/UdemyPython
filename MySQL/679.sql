select u.first_name, p.bio
from users as u
left join profiles as p
on u.id = p.user_id
where u.first_name = 'Mateus';

update users as u
left join profiles as p
on u.id = p.user_id
set p.bio = concat(p.bio, ' atualizado 1')
where u.first_name = 'Mateus';