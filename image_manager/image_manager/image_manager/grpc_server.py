import grpc
import time
from concurrent import futures
from contextlib import contextmanager

from core_lib.image_manager_grpc import image_manager_pb2_grpc, image_manager_pb2

from image_manager.image_manager.image_manager_servicer import ImageManagerServicer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


@contextmanager
def serve_forever():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_manager_pb2_grpc.add_ImageManagerServicer_to_server(ImageManagerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    yield
    server.stop(0)


def run_server():
    with serve_forever():
        print('Successfully started grpc server ')
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            pass


run_server()
