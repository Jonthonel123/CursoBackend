-- Creando nuestra base de datos
CREATE DATABASE practicas;
USE practicas

CREATE TABLE usuarios(
	id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    nombre TEXT NOT NULL,
    dni CHAR(8) UNIQUE
);

create table tareas(
	id			int		auto_increment primary key,
    titulo		varchar(100)	unique,
    descripcion text,
    usuario_id	int,
    foreign key (usuario_id) references usuarios(id)
);

-- sub lenguajes
-- DDL (data definition lenguaje)
-- DML (data manupulation language)

insert into usuarios(nombre,dni) values ('Jonthonel','70745911');
insert into usuarios(id,nombre,dni) values (default,'Carlos','15245236');
insert into usuarios(id,nombre,dni) values (default,'Manuel','15935785'),(default,'Martin','25835744'),(default,'Jose','25836974');

insert into tareas(id,titulo,descripcion,usuario_id) values (default,'Ir a la piscina','volvere a ir este fin de semana',1),(default,'Ir a la playa','volvere a ir con mis amigos',2);
insert into usuarios(id,nombre,dni) values (default,'Carlos','25478525'),(default,'Jonthonel','15824587');


INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'Ir a comer', 'Comer un sabroso pollito a la brasa', 1),
                                                                (DEFAULT, 'Comer pizza', 'Comer una sabrosa pizza con peperoni', 1);

select * from tareas;
select * from usuarios where nombre='Carlos' and id=2;

-- visualizar todas las tareas del usuario 1

select * from tareas where usuario_id=1 and titulo like '%comer%';

select * from usuarios where nombre like 'C%';
select * from usuarios where nombre like '%l';
-- Si queremos hacer la distincion entre mayuscula y minuscula antes de poner el texto colocaremos
-- la palabtra binary y esto sirve para que haga la comparacion a nivel de numeros de caracteres
select * from usuarios where nombre like binary 'J%';


