import json

def ProtoDeSerializer(data):
    """
    反序列化器，proto byte转成字典
    """
    # message = message_pb2.Message()
    # message.ParseFromString(data)
    # objs = ObjectsDeSerializer(message.objects)
    # # Converts protobuf message to JSON format.
    # message_dict = eval(MessageToJson(message, including_default_value_fields=True))
    # message_dict["objects"] = objs
    # return message_dict