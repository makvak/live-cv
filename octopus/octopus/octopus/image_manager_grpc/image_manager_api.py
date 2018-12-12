from octopus.octopus.image_manager_grpc import ImageManagerGRPCClient
from core_lib.image_manager_grpc import image_manager_pb2

# TODO refactor. It's initial testing.
im_man_client = ImageManagerGRPCClient()
response = im_man_client.client.ping(image_manager_pb2.Ping(message='loloooooolll'))
print("IT's alive!!! {}".format(response.message))


