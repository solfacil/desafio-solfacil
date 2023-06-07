#!/bin/bash

# Define directories to create
DIRS=(
    "/app/application/ports/item"
    "/app/application/ports/user"
    "/app/application/services/item"
    "/app/application/services/user"
    "/app/infrastructure/db"
    "/app/infrastructure/repositories/item"
    "/app/infrastructure/repositories/user"
    "/app/interfaces/routers"
    "/app/interfaces/schemas"
    "/app/main"
    "/app/domain/item"
    "/app/domain/user"
)

# Define files to create
FILES=(
    "/app/application/ports/item/item_repository.py"
    "/app/application/ports/user/user_repository.py"
    "/app/application/services/item/item_service.py"
    "/app/application/services/user/user_service.py"
    "/app/infrastructure/db/session.py"
    "/app/infrastructure/db/engine.py"
    "/app/infrastructure/repositories/item/sql_item_repository.py"
    "/app/infrastructure/repositories/user/sql_user_repository.py"
    "/app/interfaces/routers/item_router.py"
    "/app/interfaces/routers/user_router.py"
    "/app/interfaces/schemas/item_schema.py"
    "/app/interfaces/schemas/user_schema.py"
    "/app/main/main.py"
    "/app/domain/item/item.py"
    "/app/domain/user/user.py"
    ".env"
    "requirements.txt"
    "Dockerfile"
)

# Create directories
for dir in "${DIRS[@]}"; do
  mkdir -p "./fastapi_crud_app${dir}"
  touch "./fastapi_crud_app${dir}/__init__.py"
done

# Create files
for file in "${FILES[@]}"; do
  touch "./fastapi_crud_app${file}"
done
