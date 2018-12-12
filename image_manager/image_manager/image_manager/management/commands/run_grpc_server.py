from concurrent import futures
import time
import grpc
from contextlib import contextmanager
from django.core.management.base import BaseCommand, CommandError
from core_lib.image_manager_grpc import image_manager_pb2_grpc, image_manager_pb2
# from slimmer_grpc import main_pb2_grpc, main_pb2
# from main import models


class ImageManagerServicer(image_manager_pb2_grpc.ImageManagerServicer):
    def blur(self, request, context):
        return image_manager_pb2.Image()

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


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

@contextmanager
def serve_forever():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_manager_pb2_grpc.add_ImageManagerServicer_to_server(ImageManagerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    yield
    server.stop(0)


class Command(BaseCommand):
    help = 'api server'

    def handle(self, *args, **options):
        with serve_forever():
            self.stdout.write(self.style.SUCCESS('Successfully started grpc server '))
            try:
                while True:
                    time.sleep(_ONE_DAY_IN_SECONDS)
            except KeyboardInterrupt:
                pass
