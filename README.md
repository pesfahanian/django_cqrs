# Django CQRS

> Postgres replication taken from [here](https://github.com/eremeykin/pg-primary-replica).

# Usage

Run:

```sh
docker compose up
```

Exec into the primary container and run

```sh
psql -U user -d postgres
```

```sql
create database django_cqrs;
grant all privileges on database django_cqrs to user;
```

Exec into the replica container and run

```sh
psql -U replicator -d postgres
```

```sql
grant select on all tables in schema public to replicator;
```

Run migrations:

```sh
python manage.py migrate
```

Run server:

```sh
./scripts/run.sh
```
