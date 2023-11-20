# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from baserun.v1 import baserun_pb2 as v1_dot_baserun__pb2


class SubmissionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartRun = channel.unary_unary(
            "/baserun.v1.SubmissionService/StartRun",
            request_serializer=v1_dot_baserun__pb2.StartRunRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.StartRunResponse.FromString,
        )
        self.SubmitLog = channel.unary_unary(
            "/baserun.v1.SubmissionService/SubmitLog",
            request_serializer=v1_dot_baserun__pb2.SubmitLogRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.SubmitLogResponse.FromString,
        )
        self.SubmitSpan = channel.unary_unary(
            "/baserun.v1.SubmissionService/SubmitSpan",
            request_serializer=v1_dot_baserun__pb2.SubmitSpanRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.SubmitSpanResponse.FromString,
        )
        self.EndRun = channel.unary_unary(
            "/baserun.v1.SubmissionService/EndRun",
            request_serializer=v1_dot_baserun__pb2.EndRunRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.EndRunResponse.FromString,
        )
        self.SubmitEval = channel.unary_unary(
            "/baserun.v1.SubmissionService/SubmitEval",
            request_serializer=v1_dot_baserun__pb2.SubmitEvalRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.SubmitEvalResponse.FromString,
        )
        self.StartTestSuite = channel.unary_unary(
            "/baserun.v1.SubmissionService/StartTestSuite",
            request_serializer=v1_dot_baserun__pb2.StartTestSuiteRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.StartTestSuiteResponse.FromString,
        )
        self.EndTestSuite = channel.unary_unary(
            "/baserun.v1.SubmissionService/EndTestSuite",
            request_serializer=v1_dot_baserun__pb2.EndTestSuiteRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.EndTestSuiteResponse.FromString,
        )
        self.StartSession = channel.unary_unary(
            "/baserun.v1.SubmissionService/StartSession",
            request_serializer=v1_dot_baserun__pb2.StartSessionRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.StartSessionResponse.FromString,
        )
        self.EndSession = channel.unary_unary(
            "/baserun.v1.SubmissionService/EndSession",
            request_serializer=v1_dot_baserun__pb2.EndSessionRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.EndSessionResponse.FromString,
        )
        self.SubmitTemplateVersion = channel.unary_unary(
            "/baserun.v1.SubmissionService/SubmitTemplateVersion",
            request_serializer=v1_dot_baserun__pb2.SubmitTemplateVersionRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.SubmitTemplateVersionResponse.FromString,
        )
        self.SubmitModelConfig = channel.unary_unary(
            "/baserun.v1.SubmissionService/SubmitModelConfig",
            request_serializer=v1_dot_baserun__pb2.SubmitModelConfigRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.SubmitModelConfigResponse.FromString,
        )
        self.SubmitUser = channel.unary_unary(
            "/baserun.v1.SubmissionService/SubmitUser",
            request_serializer=v1_dot_baserun__pb2.SubmitUserRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.SubmitUserResponse.FromString,
        )
        self.GetTemplates = channel.unary_unary(
            "/baserun.v1.SubmissionService/GetTemplates",
            request_serializer=v1_dot_baserun__pb2.GetTemplatesRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.GetTemplatesResponse.FromString,
        )
        self.SubmitCapture = channel.unary_unary(
            "/baserun.v1.SubmissionService/SubmitCapture",
            request_serializer=v1_dot_baserun__pb2.SubmitCaptureRequest.SerializeToString,
            response_deserializer=v1_dot_baserun__pb2.SubmitCaptureResponse.FromString,
        )


class SubmissionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitSpan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def EndRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitEval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StartTestSuite(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def EndTestSuite(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StartSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def EndSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitTemplateVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitModelConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTemplates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitCapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SubmissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "StartRun": grpc.unary_unary_rpc_method_handler(
            servicer.StartRun,
            request_deserializer=v1_dot_baserun__pb2.StartRunRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.StartRunResponse.SerializeToString,
        ),
        "SubmitLog": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitLog,
            request_deserializer=v1_dot_baserun__pb2.SubmitLogRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.SubmitLogResponse.SerializeToString,
        ),
        "SubmitSpan": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitSpan,
            request_deserializer=v1_dot_baserun__pb2.SubmitSpanRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.SubmitSpanResponse.SerializeToString,
        ),
        "EndRun": grpc.unary_unary_rpc_method_handler(
            servicer.EndRun,
            request_deserializer=v1_dot_baserun__pb2.EndRunRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.EndRunResponse.SerializeToString,
        ),
        "SubmitEval": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitEval,
            request_deserializer=v1_dot_baserun__pb2.SubmitEvalRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.SubmitEvalResponse.SerializeToString,
        ),
        "StartTestSuite": grpc.unary_unary_rpc_method_handler(
            servicer.StartTestSuite,
            request_deserializer=v1_dot_baserun__pb2.StartTestSuiteRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.StartTestSuiteResponse.SerializeToString,
        ),
        "EndTestSuite": grpc.unary_unary_rpc_method_handler(
            servicer.EndTestSuite,
            request_deserializer=v1_dot_baserun__pb2.EndTestSuiteRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.EndTestSuiteResponse.SerializeToString,
        ),
        "StartSession": grpc.unary_unary_rpc_method_handler(
            servicer.StartSession,
            request_deserializer=v1_dot_baserun__pb2.StartSessionRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.StartSessionResponse.SerializeToString,
        ),
        "EndSession": grpc.unary_unary_rpc_method_handler(
            servicer.EndSession,
            request_deserializer=v1_dot_baserun__pb2.EndSessionRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.EndSessionResponse.SerializeToString,
        ),
        "SubmitTemplateVersion": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitTemplateVersion,
            request_deserializer=v1_dot_baserun__pb2.SubmitTemplateVersionRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.SubmitTemplateVersionResponse.SerializeToString,
        ),
        "SubmitModelConfig": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitModelConfig,
            request_deserializer=v1_dot_baserun__pb2.SubmitModelConfigRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.SubmitModelConfigResponse.SerializeToString,
        ),
        "SubmitUser": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitUser,
            request_deserializer=v1_dot_baserun__pb2.SubmitUserRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.SubmitUserResponse.SerializeToString,
        ),
        "GetTemplates": grpc.unary_unary_rpc_method_handler(
            servicer.GetTemplates,
            request_deserializer=v1_dot_baserun__pb2.GetTemplatesRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.GetTemplatesResponse.SerializeToString,
        ),
        "SubmitCapture": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitCapture,
            request_deserializer=v1_dot_baserun__pb2.SubmitCaptureRequest.FromString,
            response_serializer=v1_dot_baserun__pb2.SubmitCaptureResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "baserun.v1.SubmissionService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SubmissionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartRun(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/StartRun",
            v1_dot_baserun__pb2.StartRunRequest.SerializeToString,
            v1_dot_baserun__pb2.StartRunResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitLog(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/SubmitLog",
            v1_dot_baserun__pb2.SubmitLogRequest.SerializeToString,
            v1_dot_baserun__pb2.SubmitLogResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitSpan(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/SubmitSpan",
            v1_dot_baserun__pb2.SubmitSpanRequest.SerializeToString,
            v1_dot_baserun__pb2.SubmitSpanResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def EndRun(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/EndRun",
            v1_dot_baserun__pb2.EndRunRequest.SerializeToString,
            v1_dot_baserun__pb2.EndRunResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitEval(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/SubmitEval",
            v1_dot_baserun__pb2.SubmitEvalRequest.SerializeToString,
            v1_dot_baserun__pb2.SubmitEvalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StartTestSuite(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/StartTestSuite",
            v1_dot_baserun__pb2.StartTestSuiteRequest.SerializeToString,
            v1_dot_baserun__pb2.StartTestSuiteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def EndTestSuite(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/EndTestSuite",
            v1_dot_baserun__pb2.EndTestSuiteRequest.SerializeToString,
            v1_dot_baserun__pb2.EndTestSuiteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def StartSession(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/StartSession",
            v1_dot_baserun__pb2.StartSessionRequest.SerializeToString,
            v1_dot_baserun__pb2.StartSessionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def EndSession(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/EndSession",
            v1_dot_baserun__pb2.EndSessionRequest.SerializeToString,
            v1_dot_baserun__pb2.EndSessionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitTemplateVersion(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/SubmitTemplateVersion",
            v1_dot_baserun__pb2.SubmitTemplateVersionRequest.SerializeToString,
            v1_dot_baserun__pb2.SubmitTemplateVersionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitModelConfig(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/SubmitModelConfig",
            v1_dot_baserun__pb2.SubmitModelConfigRequest.SerializeToString,
            v1_dot_baserun__pb2.SubmitModelConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitUser(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/SubmitUser",
            v1_dot_baserun__pb2.SubmitUserRequest.SerializeToString,
            v1_dot_baserun__pb2.SubmitUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetTemplates(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/GetTemplates",
            v1_dot_baserun__pb2.GetTemplatesRequest.SerializeToString,
            v1_dot_baserun__pb2.GetTemplatesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitCapture(
            request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/baserun.v1.SubmissionService/SubmitCapture",
            v1_dot_baserun__pb2.SubmitCaptureRequest.SerializeToString,
            v1_dot_baserun__pb2.SubmitCaptureResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
