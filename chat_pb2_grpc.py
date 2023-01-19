# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

# Added path
from . import chat_pb2 as chat__pb2

class ChatServiceStub(object):
    """create services
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendMessage = channel.unary_unary(
                '/package.chat.ChatService/sendMessage',
                request_serializer=chat__pb2.sendMessageRequest.SerializeToString,
                response_deserializer=chat__pb2.sendMessageResponce.FromString,
                )
        self.getUsers = channel.unary_unary(
                '/package.chat.ChatService/getUsers',
                request_serializer=chat__pb2.getUsersRequest.SerializeToString,
                response_deserializer=chat__pb2.getUsersResponce.FromString,
                )
        self.getMessages = channel.unary_stream(
                '/package.chat.ChatService/getMessages',
                request_serializer=chat__pb2.getMessagesRequest.SerializeToString,
                response_deserializer=chat__pb2.getMessagesResponce.FromString,
                )


class ChatServiceServicer(object):
    """create services
    """

    def sendMessage(self, request, context):
        """create grpc method
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.sendMessage,
                    request_deserializer=chat__pb2.sendMessageRequest.FromString,
                    response_serializer=chat__pb2.sendMessageResponce.SerializeToString,
            ),
            'getUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.getUsers,
                    request_deserializer=chat__pb2.getUsersRequest.FromString,
                    response_serializer=chat__pb2.getUsersResponce.SerializeToString,
            ),
            'getMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.getMessages,
                    request_deserializer=chat__pb2.getMessagesRequest.FromString,
                    response_serializer=chat__pb2.getMessagesResponce.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'package.chat.ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """create services
    """

    @staticmethod
    def sendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/package.chat.ChatService/sendMessage',
            chat__pb2.sendMessageRequest.SerializeToString,
            chat__pb2.sendMessageResponce.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/package.chat.ChatService/getUsers',
            chat__pb2.getUsersRequest.SerializeToString,
            chat__pb2.getUsersResponce.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/package.chat.ChatService/getMessages',
            chat__pb2.getMessagesRequest.SerializeToString,
            chat__pb2.getMessagesResponce.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
