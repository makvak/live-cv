from cv_lib.models import Image


# here we will have handlers on cv actions with images

class BaseImageHandler(object):

    def __init__(self, image):
        self.image = image

    def execute(self):
        raise NotImplemented


class BlurFilterHandler(BaseImageHandler):

    def execute(self):
        pass
