select u.first_name, p.bio
from users as u
left join profiles as p
on u.id = p.user_id
where u.first_name = 'Mateus';

delete p
from users as u
left join profiles as p
on u.id = p.user_id
where u.first_name = 'Mateus';