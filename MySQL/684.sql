-- 1
insert into users (first_name, email, password_hash)
values ('Marcia', 'marcia@email.com', 'djh4AJBbrj2AS'),
       ('Jaqueline', 'jaqueline@email.com', 'jhASJDHhi42142'),
       ('Almir', 'almir@email.com', '1Q#JQj42h244'),
       ('Gabriele', 'gabriele@email.com', '21jhnJQ@H$I!@4h'),
       ('Godofredo', 'godofredo@email.com', 'JRNI!@QJ$Nrnjaoishnrd4');

-- 2
insert into profiles (bio, user_id)
select concat('Bio de ', first_name), id
from users
where id in (121, 122, 123, 124, 125);

-- 3
insert into users_roles (user_id, role_id)
select u.id, r.id
from users as u, roles as r
where u.id in (121, 122, 123, 124, 125)
order by rand()
limit 15;

-- 4
select * from users
order by id desc
limit 5;

-- 5
update users
set salary = 5478.15
where id = 125;

-- 6
delete from users_roles
order by rand()
limit 1;

-- 7
select u.id, u.first_name, ur.user_id, ur.role_id, r.name as role_name
from users as u
    inner join users_roles as ur on u.id = ur.user_id
    inner join roles as r on r.id = ur.role_id
where r.name = 'PUT'
order by rand()
limit 1;

delete from users as u
where id in (
    select u.id, u.first_name, ur.user_id, ur.role_id, r.name as role_name
    from users as u
        inner join users_roles as ur on u.id = ur.user_id
        inner join roles as r on r.id = ur.role_id
    where r.name = 'PUT'
    order by rand()
    limit 1
);

-- 8
select u.id, u.first_name, p.bio, p.user_id, ur.user_id, r.name as role_name
from users as u
inner join profiles as p on u.id = p.user_id
inner join users_roles as ur on u.id = ur.user_id
inner join roles as r on r.id = ur.role_id
order by u.id;

-- 9
select u.id, u.first_name, p.bio, p.user_id, ur.user_id, r.name as role_name
from users as u
left join profiles as p on u.id = p.user_id
left join users_roles as ur on u.id = ur.user_id
left join roles as r on r.id = ur.role_id
order by u.id;

-- 10
select u.id, u.first_name, p.bio, p.user_id, ur.user_id, r.name as role_name, u.salary
from users as u
inner join profiles as p on u.id = p.user_id
inner join users_roles as ur on u.id = ur.user_id
inner join roles as r on r.id = ur.role_id
order by u.salary desc;
