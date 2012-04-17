drop table if exists urls;

create table urls (
	id integer primary key autoincrement
	, longurl string not null
);
