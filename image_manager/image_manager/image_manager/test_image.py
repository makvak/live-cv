from sqlalchemy_imageattach.context import store_context
from cv_lib.models.image import store, Image
from cv_lib.models.base import session_factory

# TODO module
def run_test():
    session = session_factory()
    with store_context(store):
        with open('path_to_file', 'rb') as f:
            image = Image()
            image.picture.from_file(f)
            session.add(image)
        session.commit()
    session.close()

run_test()