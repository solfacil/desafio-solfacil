from threading import Lock

from loguru import logger  # noqa: F401
from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import sessionmaker  # noqa: F401
from sqlalchemy.orm.session import Session


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class DB(metaclass=SingletonMeta):
    engine = None

    @classmethod
    def get_session(cls, autocommit=False, autoflush=False, expire_on_commit=False):
        if cls.engine is None:
            raise ConnectionError("Please connect to db before getting an session")

        Session = sessionmaker(bind=cls.engine, autocommit=autocommit, autoflush=autoflush, expire_on_commit=expire_on_commit)
        return Session

    @classmethod
    def connect(cls, **kwargs):
        """
        Input:
            drivername
            username
            password
            host
            port
            database
        """
        database = kwargs.pop('database')
        if kwargs.get('drivername') != 'sqlite':
            # connect without database arg and try to create the database if not exists
            DB_URL = URL.create(**kwargs)
            cls.engine = create_engine(DB_URL)

            with cls.get_session().begin() as session:
                session.execute(text(f"CREATE DATABASE IF NOT EXISTS {database}"))

        # then reconnect using database argument
        # and update engine with the new URL
        DB_URL = URL.create(**kwargs, database=database)
        logger.critical(f"{DB_URL = }")
        cls.engine = create_engine(DB_URL)
        return True

    @classmethod
    async def get_db(cls) -> Session:
        Session = cls.get_session()
        with Session() as session:
            yield session
