import cv2
import numpy as np

from typing import ByteString


def blur(src_image: ByteString, kernel_side: int = 5) -> ByteString:
    src_np_data = np.fromstring(src_image, np.uint8)
    src_data = cv2.imdecode(src_np_data, cv2.IMREAD_COLOR)
    dst_np_data = cv2.blur(src_data, (kernel_side, kernel_side))
    dst_data = cv2.imencode(".jpg", dst_np_data)[1].tostring()
    return dst_data
