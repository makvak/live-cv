from typing import List
from collections import namedtuple
from sqlalchemy_imageattach.context import store_context
from sqlalchemy_utils.types.uuid import UUIDType

from cv_lib.db_session import construct_session, session_factory
from cv_lib.image_handler import BlurFilterHandler
from cv_lib.models.image import store, ImageContainer

from sqlalchemy.orm import Session

ImageData = namedtuple('ImageData', 'data, uuid')


def create_image(data) -> ImageData:
    return None


@construct_session
def get_images(uuids: List[UUIDType], session: Session) -> List[ImageData]:
    return session.query(ImageContainer).filter(ImageContainer.uuid.in_(uuids)).all()


@construct_session
def blur_image(uuid: UUIDType, session: Session) -> ImageData:
    with store_context(store):
        image_container: ImageContainer = session.query(ImageContainer).get(uuid)
        new_image_container: ImageContainer = BlurFilterHandler(image_container).execute()
        session.add(new_image_container)
        image_data = ImageData(data=new_image_container.image.open_file(), uuid=str(new_image_container.uuid))
        session.commit()
        return image_data
