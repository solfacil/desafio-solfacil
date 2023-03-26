from loguru import logger
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import Session


class Base(DeclarativeBase):

    @classmethod
    def create_or_update(cls, db: Session, data: dict, **filters):
        """Query the database and inser/update fields based on filters, just like filter_by does
        Filters with db.query(cls).filter_by(**filters).first()
        so if you want a Partner with a cnpj, filters would be `cnpj=TARGET_CNPJ`\n
        `data` is a dict with data to build or update the model, this should mainly be the Pydantic model .dict() of the class
        """
        is_new = False
        in_db = db.query(cls).filter_by(**filters).first()
        if in_db:
            logger.debug(f"{cls.__name__} already exists, trying to update fields if any needs to")
            for field, value in data.items():
                if hasattr(in_db, field):
                    value_before = getattr(in_db, field)
                    if value != value_before:
                        setattr(in_db, field, value)
                        # could be used for audit changes that user did if inserted in another db
                        logger.debug(f"Updating {cls.__name__} id:{in_db.id} -> [{field}] was '{value_before}', updating to: '{value}'")
        else:
            # its a new object, just adding
            is_new = True
            logger.debug(f"Creating new '{cls.__name__}' with {data = }")
            in_db = cls(**data)

        db.add(in_db)
        db.commit()
        db.refresh(in_db)
        return in_db, is_new
