# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/tenant.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.talent_v4beta1.proto import (
    common_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/tenant.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.talent.v4beta1B\023TenantResourceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS"
    ),
    serialized_pb=_b(
        '\n.google/cloud/talent_v4beta1/proto/tenant.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a.google/cloud/talent_v4beta1/proto/common.proto\x1a\x1cgoogle/api/annotations.proto"\xf8\x01\n\x06Tenant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x02 \x01(\t\x12\x45\n\nusage_type\x18\x03 \x01(\x0e\x32\x31.google.cloud.talent.v4beta1.Tenant.DataUsageType\x12\x34\n,keyword_searchable_profile_custom_attributes\x18\x04 \x03(\t"N\n\rDataUsageType\x12\x1f\n\x1b\x44\x41TA_USAGE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nAGGREGATED\x10\x01\x12\x0c\n\x08ISOLATED\x10\x02\x42\x81\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x13TenantResourceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TENANT_DATAUSAGETYPE = _descriptor.EnumDescriptor(
    name="DataUsageType",
    full_name="google.cloud.talent.v4beta1.Tenant.DataUsageType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="DATA_USAGE_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="AGGREGATED", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ISOLATED", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=328,
    serialized_end=406,
)
_sym_db.RegisterEnumDescriptor(_TENANT_DATAUSAGETYPE)


_TENANT = _descriptor.Descriptor(
    name="Tenant",
    full_name="google.cloud.talent.v4beta1.Tenant",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.Tenant.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="external_id",
            full_name="google.cloud.talent.v4beta1.Tenant.external_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="usage_type",
            full_name="google.cloud.talent.v4beta1.Tenant.usage_type",
            index=2,
            number=3,
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
            name="keyword_searchable_profile_custom_attributes",
            full_name="google.cloud.talent.v4beta1.Tenant.keyword_searchable_profile_custom_attributes",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
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
    enum_types=[_TENANT_DATAUSAGETYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=158,
    serialized_end=406,
)

_TENANT.fields_by_name["usage_type"].enum_type = _TENANT_DATAUSAGETYPE
_TENANT_DATAUSAGETYPE.containing_type = _TENANT
DESCRIPTOR.message_types_by_name["Tenant"] = _TENANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tenant = _reflection.GeneratedProtocolMessageType(
    "Tenant",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TENANT,
        __module__="google.cloud.talent_v4beta1.proto.tenant_pb2",
        __doc__="""A Tenant resource represents a tenant in the service. A tenant is a
  group or entity that shares common access with specific privileges for
  resources like profiles. Customer may create multiple tenants to provide
  data isolation for different groups.
  
  
  Attributes:
      name:
          Required during tenant update.  The resource name for a
          tenant. This is generated by the service when a tenant is
          created.  The format is
          "projects/{project\_id}/tenants/{tenant\_id}", for example,
          "projects/api-test-project/tenants/foo".
      external_id:
          Required.  Client side tenant identifier, used to uniquely
          identify the tenant.  The maximum number of allowed characters
          is 255.
      usage_type:
          Optional.  Indicates whether data owned by this tenant may be
          used to provide product improvements across other tenants.
          Defaults behavior is [DataUsageType.ISOLATED][google.cloud.tal
          ent.v4beta1.Tenant.DataUsageType.ISOLATED] if it's unset.
      keyword_searchable_profile_custom_attributes:
          Optional.  A list of keys of filterable [Profile.custom\_attri
          butes][google.cloud.talent.v4beta1.Profile.custom\_attributes]
          , whose corresponding ``string_values`` are used in keyword
          searches. Profiles with ``string_values`` under these
          specified field keys are returned if any of the values match
          the search keyword. Custom field values with parenthesis,
          brackets and special symbols are not searchable as-is, and
          must be surrounded by quotes.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.Tenant)
    ),
)
_sym_db.RegisterMessage(Tenant)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
