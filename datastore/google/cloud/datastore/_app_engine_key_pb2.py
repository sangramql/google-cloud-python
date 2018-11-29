# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _app_engine_key.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="_app_engine_key.proto",
    package="",
    syntax="proto2",
    serialized_pb=_b(
        '\n\x15_app_engine_key.proto"V\n\tReference\x12\x0b\n\x03\x61pp\x18\r \x02(\t\x12\x12\n\nname_space\x18\x14 \x01(\t\x12\x13\n\x04path\x18\x0e \x02(\x0b\x32\x05.Path\x12\x13\n\x0b\x64\x61tabase_id\x18\x17 \x01(\t"Y\n\x04Path\x12\x1e\n\x07\x65lement\x18\x01 \x03(\n2\r.Path.Element\x1a\x31\n\x07\x45lement\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\n\n\x02id\x18\x03 \x01(\x03\x12\x0c\n\x04name\x18\x04 \x01(\t'
    ),
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


_REFERENCE = _descriptor.Descriptor(
    name="Reference",
    full_name="Reference",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="app",
            full_name="Reference.app",
            index=0,
            number=13,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="name_space",
            full_name="Reference.name_space",
            index=1,
            number=20,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="path",
            full_name="Reference.path",
            index=2,
            number=14,
            type=11,
            cpp_type=10,
            label=2,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="database_id",
            full_name="Reference.database_id",
            index=3,
            number=23,
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=25,
    serialized_end=111,
)


_PATH_ELEMENT = _descriptor.Descriptor(
    name="Element",
    full_name="Path.Element",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="Path.Element.type",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="Path.Element.id",
            index=1,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="Path.Element.name",
            index=2,
            number=4,
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=153,
    serialized_end=202,
)

_PATH = _descriptor.Descriptor(
    name="Path",
    full_name="Path",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="element",
            full_name="Path.element",
            index=0,
            number=1,
            type=10,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        )
    ],
    extensions=[],
    nested_types=[_PATH_ELEMENT],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=113,
    serialized_end=202,
)

_REFERENCE.fields_by_name["path"].message_type = _PATH
_PATH_ELEMENT.containing_type = _PATH
_PATH.fields_by_name["element"].message_type = _PATH_ELEMENT
DESCRIPTOR.message_types_by_name["Reference"] = _REFERENCE
DESCRIPTOR.message_types_by_name["Path"] = _PATH

Reference = _reflection.GeneratedProtocolMessageType(
    "Reference",
    (_message.Message,),
    dict(
        DESCRIPTOR=_REFERENCE,
        __module__="_app_engine_key_pb2"
        # @@protoc_insertion_point(class_scope:Reference)
    ),
)
_sym_db.RegisterMessage(Reference)

Path = _reflection.GeneratedProtocolMessageType(
    "Path",
    (_message.Message,),
    dict(
        Element=_reflection.GeneratedProtocolMessageType(
            "Element",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PATH_ELEMENT,
                __module__="_app_engine_key_pb2"
                # @@protoc_insertion_point(class_scope:Path.Element)
            ),
        ),
        DESCRIPTOR=_PATH,
        __module__="_app_engine_key_pb2"
        # @@protoc_insertion_point(class_scope:Path)
    ),
)
_sym_db.RegisterMessage(Path)
_sym_db.RegisterMessage(Path.Element)


# @@protoc_insertion_point(module_scope)
