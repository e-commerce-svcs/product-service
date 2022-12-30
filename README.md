# product-service

## Setup

### Autogenerate a new migration

```sh
python -m alembic revision --autogenerate -m "Add power to Hero model"
```

### Apply the migration

```sh
python -m alembic upgrade head
```
