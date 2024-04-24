create database django_cqrs;
grant all privileges on database django_cqrs to user;
grant select on all tables in schema public to replicator;
