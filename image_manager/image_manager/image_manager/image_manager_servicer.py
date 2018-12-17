from core_lib.image_manager_grpc import image_manager_pb2_grpc, image_manager_pb2
from cv_lib.domain.image import (
    blur_image,
    ImageData
)

CHUNK_SIZE = 1024 * 1024


class ImageManagerServicer(image_manager_pb2_grpc.ImageManagerServicer):
    def blur(self, request, context):

        image_data = blur_image(request.uuid)
        # metadata = context.invocation_metadata()
        # metadata['uuid'] = image_data.uuid
        # metadata['success'] = 1
        # pass
        # for bunch in image_data.data:
        #     # image_manager_pb2.Image(image=bunch, success=True, uuid=image_data.uuid)
        #     image_manager_pb2.Image(image=bunch)
        while True:
            chunk = image_data.data.read(CHUNK_SIZE)
            if len(chunk) == 0:
                return
            yield image_manager_pb2.Image(image=chunk)

    def ping(self, request, context):
        return image_manager_pb2.Pong(message=request.message)
    # def ping(self, request, context):
    #     return main_pb2.Pong(message=request.message)
    #
    # def new_system_run(self, request, context):
    #     # your code here
    #     return main_pb2.SystemRunResponse(run_id="your id")
    #
    # def new_activation(self, request, context):
    #     # your code here
    #     return main_pb2.ActivationResponse(success=True)