import uuid

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.uuid import UUIDType
from sqlalchemy_imageattach.entity import Image as AlchemyImage, image_attachment
from sqlalchemy_imageattach.stores import fs

from django.conf import settings

from .base import Base

store = fs.FileSystemStore(
    path='/images/'.format(settings.BASE_DIR),
    base_url='127.0.0.1:8003/images/'
)


class ImageContainer(Base):
    __tablename__ = 'image_container'
    uuid = Column(UUIDType, default=uuid.uuid4, primary_key=True)
    image = image_attachment('Image')


class Image(Base, AlchemyImage):
    image_container_uuid = Column(UUIDType, ForeignKey('image_container.uuid'), primary_key=True)
    image_container = relationship('ImageContainer')
    __tablename__ = 'image'
