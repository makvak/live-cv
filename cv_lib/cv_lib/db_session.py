from sqlalchemy.orm import (
    Session,
    sessionmaker
)

from cv_lib.models.base import (
    Base,
    engine
)

_SessionFactory = sessionmaker(bind=engine)


def session_factory() -> Session:
    Base.metadata.create_all(engine)
    return _SessionFactory()


def construct_session(func):
    def func_wrapper(*args, **kwargs):
        session = session_factory()
        result = func(*args,  session=session, **kwargs)
        session.close()
        return result
    return func_wrapper
