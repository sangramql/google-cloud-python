# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/storage_v1beta1/proto/read_options.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigquery/storage_v1beta1/proto/read_options.proto",
    package="google.cloud.bigquery.storage.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n)com.google.cloud.bigquery.storage.v1beta1ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storage"
    ),
    serialized_pb=_b(
        '\n>google/cloud/bigquery/storage_v1beta1/proto/read_options.proto\x12%google.cloud.bigquery.storage.v1beta1"D\n\x10TableReadOptions\x12\x17\n\x0fselected_fields\x18\x01 \x03(\t\x12\x17\n\x0frow_restriction\x18\x02 \x01(\tBy\n)com.google.cloud.bigquery.storage.v1beta1ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storageb\x06proto3'
    ),
)


_TABLEREADOPTIONS = _descriptor.Descriptor(
    name="TableReadOptions",
    full_name="google.cloud.bigquery.storage.v1beta1.TableReadOptions",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="selected_fields",
            full_name="google.cloud.bigquery.storage.v1beta1.TableReadOptions.selected_fields",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="row_restriction",
            full_name="google.cloud.bigquery.storage.v1beta1.TableReadOptions.row_restriction",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=105,
    serialized_end=173,
)

DESCRIPTOR.message_types_by_name["TableReadOptions"] = _TABLEREADOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TableReadOptions = _reflection.GeneratedProtocolMessageType(
    "TableReadOptions",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TABLEREADOPTIONS,
        __module__="google.cloud.bigquery.storage_v1beta1.proto.read_options_pb2",
        __doc__="""Options dictating how we read a table.
  
  
  Attributes:
      selected_fields:
          Optional. Names of the fields in the table that should be
          read. If empty, all fields will be read. If the specified
          field is a nested field, all the sub-fields in the field will
          be selected. The output field order is unrelated to the order
          of fields in selected\_fields.
      row_restriction:
          Optional. SQL text filtering statement, similar to a WHERE
          clause in a query. Currently, we support combinations of
          predicates that are a comparison between a column and a
          constant value in SQL statement. Aggregates are not supported.
          Example: "a > DATE '2014-9-27' AND (b > 5 and C LIKE 'date')"
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta1.TableReadOptions)
    ),
)
_sym_db.RegisterMessage(TableReadOptions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
