"""create parceiro table

Revision ID: 22badcb1685a
Revises: 
Create Date: 2023-06-06 20:50:03.833581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22badcb1685a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "parceiro",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("cnpj", sa.String(14), unique=True, index=True, nullable=False),
        sa.Column("razao_social", sa.String(255), nullable=False),
        sa.Column("nome_fantasia", sa.String(255)),
        sa.Column("telefone", sa.String(11)),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("cep", sa.String(8), nullable=False),
        sa.Column("cidade", sa.String(255), nullable=True),
        sa.Column("estado", sa.String(2), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("parceiro")
