# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transExplorer_pb2 as transExplorer__pb2


class TransExplorerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OpenConnection = channel.unary_unary(
                '/shai.TransExplorer/OpenConnection',
                request_serializer=transExplorer__pb2.ConnectRequest.SerializeToString,
                response_deserializer=transExplorer__pb2.Connection.FromString,
                )
        self.LoadModel = channel.unary_unary(
                '/shai.TransExplorer/LoadModel',
                request_serializer=transExplorer__pb2.LoadModelRequest.SerializeToString,
                response_deserializer=transExplorer__pb2.LoadModelResponse.FromString,
                )


class TransExplorerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OpenConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadModel(self, request, context):
        """TODO rpc Terminate (TerminateRequest) returns (TerminationReply) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransExplorerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OpenConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenConnection,
                    request_deserializer=transExplorer__pb2.ConnectRequest.FromString,
                    response_serializer=transExplorer__pb2.Connection.SerializeToString,
            ),
            'LoadModel': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadModel,
                    request_deserializer=transExplorer__pb2.LoadModelRequest.FromString,
                    response_serializer=transExplorer__pb2.LoadModelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'shai.TransExplorer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransExplorer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OpenConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shai.TransExplorer/OpenConnection',
            transExplorer__pb2.ConnectRequest.SerializeToString,
            transExplorer__pb2.Connection.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shai.TransExplorer/LoadModel',
            transExplorer__pb2.LoadModelRequest.SerializeToString,
            transExplorer__pb2.LoadModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
