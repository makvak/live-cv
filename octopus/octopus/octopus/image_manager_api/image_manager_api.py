from octopus.octopus.image_manager_api import ImageManagerGRPCClient
from core_lib.image_manager_grpc import image_manager_pb2

# TODO refactor. It's initial testing.
uuid = '5e6853c6-e762-41e1-8717-0d8a3fac49d6'
im_man_client = ImageManagerGRPCClient()
response = im_man_client.client.blur(image_manager_pb2.Uuid(uuid=uuid))
with open('lol.jpg', 'wb') as f:
    for chunk in response:
        f.write(chunk.image)
response_1 = im_man_client.client.ping(image_manager_pb2.Ping(message='loloooooolll'))
# print("IT's alive!!! {}".format(response.message))


