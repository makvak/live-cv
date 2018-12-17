import grpc
from core_lib.image_manager_grpc import (
    image_manager_pb2,
    image_manager_pb2_grpc
)


class ImageManagerGRPCClient(object):
    # TODO refactor, add mock client. Add server and port as parameter
    def __init__(self):
        self.channel = grpc.insecure_channel('127.0.0.1:50051')
        self.client = image_manager_pb2_grpc.ImageManagerStub(self.channel)
