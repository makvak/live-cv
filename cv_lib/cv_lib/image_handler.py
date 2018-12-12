from cv_lib.models import ImageContainer
from .image_processor import blur


class BaseImageHandler(object):

    def __init__(self, image_container):
        self.image_container = image_container

    def execute(self):
        raise NotImplemented


class BlurFilterHandler(BaseImageHandler):

    def execute(self) -> ImageContainer:
        src_data = blur(self.image_container.image.make_blob())
        new_image_container = ImageContainer()
        new_image_container.image.from_blob(src_data)
        return new_image_container
