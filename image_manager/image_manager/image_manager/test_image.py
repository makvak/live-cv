from sqlalchemy_imageattach.context import store_context
from cv_lib.models.image import store, Image, ImageContainer
from cv_lib.db_session import session_factory

from cv_lib.image_handler import BlurFilterHandler

# TODO remove module
def put_image():
    session = session_factory()
    with store_context(store):
        with open('path to file', 'rb') as f:
            image_c = ImageContainer()
            image_c.image.from_file(f)
            session.add(image_c)
        session.commit()
    session.close()


def perform_blur():
    from cv_lib.domain.image import blur_image
    session = session_factory()
    uuid = session.query(ImageContainer).first().uuid
    session.close()
    blur_image(session.query(ImageContainer).first().uuid)
    # session = session_factory()
    # with store_context(store):
    #     image_c = session.query(ImageContainer).first()
    #     new_i_c = BlurFilterHandler(image_c).execute()
    #     session.add(new_i_c)
    #     session.commit()
    # session.close()

# put_image()
perform_blur()