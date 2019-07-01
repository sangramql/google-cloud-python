# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas_v1/proto/discovery.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from grafeas.grafeas_v1.proto import common_pb2 as grafeas__v1_dot_proto_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="grafeas_v1/proto/discovery.proto",
    package="grafeas.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA"
    ),
    serialized_pb=_b(
        '\n grafeas_v1/proto/discovery.proto\x12\ngrafeas.v1\x1a\x17google/rpc/status.proto\x1a\x1dgrafeas_v1/proto/common.proto"<\n\rDiscoveryNote\x12+\n\ranalysis_kind\x18\x01 \x01(\x0e\x32\x14.grafeas.v1.NoteKind"\xcb\x03\n\x13\x44iscoveryOccurrence\x12O\n\x13\x63ontinuous_analysis\x18\x01 \x01(\x0e\x32\x32.grafeas.v1.DiscoveryOccurrence.ContinuousAnalysis\x12G\n\x0f\x61nalysis_status\x18\x02 \x01(\x0e\x32..grafeas.v1.DiscoveryOccurrence.AnalysisStatus\x12\x31\n\x15\x61nalysis_status_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status"S\n\x12\x43ontinuousAnalysis\x12#\n\x1f\x43ONTINUOUS_ANALYSIS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02"\x91\x01\n\x0e\x41nalysisStatus\x12\x1f\n\x1b\x41NALYSIS_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08SCANNING\x10\x02\x12\x14\n\x10\x46INISHED_SUCCESS\x10\x03\x12\x13\n\x0f\x46INISHED_FAILED\x10\x04\x12\x18\n\x14\x46INISHED_UNSUPPORTED\x10\x05\x42Q\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
    ),
    dependencies=[
        google_dot_rpc_dot_status__pb2.DESCRIPTOR,
        grafeas__v1_dot_proto_dot_common__pb2.DESCRIPTOR,
    ],
)


_DISCOVERYOCCURRENCE_CONTINUOUSANALYSIS = _descriptor.EnumDescriptor(
    name="ContinuousAnalysis",
    full_name="grafeas.v1.DiscoveryOccurrence.ContinuousAnalysis",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CONTINUOUS_ANALYSIS_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACTIVE", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INACTIVE", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=395,
    serialized_end=478,
)
_sym_db.RegisterEnumDescriptor(_DISCOVERYOCCURRENCE_CONTINUOUSANALYSIS)

_DISCOVERYOCCURRENCE_ANALYSISSTATUS = _descriptor.EnumDescriptor(
    name="AnalysisStatus",
    full_name="grafeas.v1.DiscoveryOccurrence.AnalysisStatus",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ANALYSIS_STATUS_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PENDING", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SCANNING", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="FINISHED_SUCCESS",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="FINISHED_FAILED",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="FINISHED_UNSUPPORTED",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=481,
    serialized_end=626,
)
_sym_db.RegisterEnumDescriptor(_DISCOVERYOCCURRENCE_ANALYSISSTATUS)


_DISCOVERYNOTE = _descriptor.Descriptor(
    name="DiscoveryNote",
    full_name="grafeas.v1.DiscoveryNote",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="analysis_kind",
            full_name="grafeas.v1.DiscoveryNote.analysis_kind",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=104,
    serialized_end=164,
)


_DISCOVERYOCCURRENCE = _descriptor.Descriptor(
    name="DiscoveryOccurrence",
    full_name="grafeas.v1.DiscoveryOccurrence",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="continuous_analysis",
            full_name="grafeas.v1.DiscoveryOccurrence.continuous_analysis",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="analysis_status",
            full_name="grafeas.v1.DiscoveryOccurrence.analysis_status",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="analysis_status_error",
            full_name="grafeas.v1.DiscoveryOccurrence.analysis_status_error",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _DISCOVERYOCCURRENCE_CONTINUOUSANALYSIS,
        _DISCOVERYOCCURRENCE_ANALYSISSTATUS,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=167,
    serialized_end=626,
)

_DISCOVERYNOTE.fields_by_name[
    "analysis_kind"
].enum_type = grafeas__v1_dot_proto_dot_common__pb2._NOTEKIND
_DISCOVERYOCCURRENCE.fields_by_name[
    "continuous_analysis"
].enum_type = _DISCOVERYOCCURRENCE_CONTINUOUSANALYSIS
_DISCOVERYOCCURRENCE.fields_by_name[
    "analysis_status"
].enum_type = _DISCOVERYOCCURRENCE_ANALYSISSTATUS
_DISCOVERYOCCURRENCE.fields_by_name[
    "analysis_status_error"
].message_type = google_dot_rpc_dot_status__pb2._STATUS
_DISCOVERYOCCURRENCE_CONTINUOUSANALYSIS.containing_type = _DISCOVERYOCCURRENCE
_DISCOVERYOCCURRENCE_ANALYSISSTATUS.containing_type = _DISCOVERYOCCURRENCE
DESCRIPTOR.message_types_by_name["DiscoveryNote"] = _DISCOVERYNOTE
DESCRIPTOR.message_types_by_name["DiscoveryOccurrence"] = _DISCOVERYOCCURRENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiscoveryNote = _reflection.GeneratedProtocolMessageType(
    "DiscoveryNote",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DISCOVERYNOTE,
        __module__="grafeas_v1.proto.discovery_pb2",
        __doc__="""A note that indicates a type of analysis a provider would perform. This
  note exists in a provider's project. A ``Discovery`` occurrence is
  created in a consumer's project at the start of analysis.
  
  
  Attributes:
      analysis_kind:
          Required. Immutable. The kind of analysis that is handled by
          this discovery.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.DiscoveryNote)
    ),
)
_sym_db.RegisterMessage(DiscoveryNote)

DiscoveryOccurrence = _reflection.GeneratedProtocolMessageType(
    "DiscoveryOccurrence",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DISCOVERYOCCURRENCE,
        __module__="grafeas_v1.proto.discovery_pb2",
        __doc__="""Provides information about the analysis status of a discovered resource.
  
  
  Attributes:
      continuous_analysis:
          Whether the resource is continuously analyzed.
      analysis_status:
          The status of discovery for the resource.
      analysis_status_error:
          When an error is encountered this will contain a
          LocalizedMessage under details to show to the user. The
          LocalizedMessage is output only and populated by the API.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.DiscoveryOccurrence)
    ),
)
_sym_db.RegisterMessage(DiscoveryOccurrence)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
