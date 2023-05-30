sleep 20
python -m alembic revision --autogenerate -m "initial"
python -m alembic upgrade head
