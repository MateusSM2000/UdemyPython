# comentário
-- comentario
/* comentario */

show tables; -- mostra as tabelas da base de dados
describe users; -- descreve as colunas da tabela
insert into users
    (first_name, last_name, email, password_hash) values
        ("Luiz", "Miranda", "sdadssdas@gmail.com", "pw_hash2"),
        ("Luiz", "Miranda", "sdadssda323s@gmail.com", "pw_hash3"),
        ("Luiz", "Miranda", "sdadss2323232das@gmail.com", "pw_hash4"); -- inseri registros na base de dados