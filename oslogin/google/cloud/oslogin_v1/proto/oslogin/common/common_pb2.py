# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/oslogin/common/common.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/oslogin/common/common.proto",
    package="google.cloud.oslogin.common",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.oslogin.commonB\014OsLoginProtoZAgoogle.golang.org/genproto/googleapis/cloud/oslogin/common;common\252\002\033Google.Cloud.OsLogin.Common\312\002\033Google\\Cloud\\OsLogin\\Common"
    ),
    serialized_pb=_b(
        '\n(google/cloud/oslogin/common/common.proto\x12\x1bgoogle.cloud.oslogin.common\x1a\x1cgoogle/api/annotations.proto"\xa8\x01\n\x0cPosixAccount\x12\x0f\n\x07primary\x18\x01 \x01(\x08\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\x03\x12\x0b\n\x03gid\x18\x04 \x01(\x03\x12\x16\n\x0ehome_directory\x18\x05 \x01(\t\x12\r\n\x05shell\x18\x06 \x01(\t\x12\r\n\x05gecos\x18\x07 \x01(\t\x12\x11\n\tsystem_id\x18\x08 \x01(\t\x12\x12\n\naccount_id\x18\t \x01(\t"N\n\x0cSshPublicKey\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x14\x65xpiration_time_usec\x18\x02 \x01(\x03\x12\x13\n\x0b\x66ingerprint\x18\x03 \x01(\tB\xae\x01\n\x1f\x63om.google.cloud.oslogin.commonB\x0cOsLoginProtoZAgoogle.golang.org/genproto/googleapis/cloud/oslogin/common;common\xaa\x02\x1bGoogle.Cloud.OsLogin.Common\xca\x02\x1bGoogle\\Cloud\\OsLogin\\Commonb\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_POSIXACCOUNT = _descriptor.Descriptor(
    name="PosixAccount",
    full_name="google.cloud.oslogin.common.PosixAccount",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="primary",
            full_name="google.cloud.oslogin.common.PosixAccount.primary",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="username",
            full_name="google.cloud.oslogin.common.PosixAccount.username",
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
            name="uid",
            full_name="google.cloud.oslogin.common.PosixAccount.uid",
            index=2,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="gid",
            full_name="google.cloud.oslogin.common.PosixAccount.gid",
            index=3,
            number=4,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="home_directory",
            full_name="google.cloud.oslogin.common.PosixAccount.home_directory",
            index=4,
            number=5,
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
            name="shell",
            full_name="google.cloud.oslogin.common.PosixAccount.shell",
            index=5,
            number=6,
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
            name="gecos",
            full_name="google.cloud.oslogin.common.PosixAccount.gecos",
            index=6,
            number=7,
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
            name="system_id",
            full_name="google.cloud.oslogin.common.PosixAccount.system_id",
            index=7,
            number=8,
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
            name="account_id",
            full_name="google.cloud.oslogin.common.PosixAccount.account_id",
            index=8,
            number=9,
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
    serialized_start=104,
    serialized_end=272,
)


_SSHPUBLICKEY = _descriptor.Descriptor(
    name="SshPublicKey",
    full_name="google.cloud.oslogin.common.SshPublicKey",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.oslogin.common.SshPublicKey.key",
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
            name="expiration_time_usec",
            full_name="google.cloud.oslogin.common.SshPublicKey.expiration_time_usec",
            index=1,
            number=2,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fingerprint",
            full_name="google.cloud.oslogin.common.SshPublicKey.fingerprint",
            index=2,
            number=3,
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
    serialized_start=274,
    serialized_end=352,
)

DESCRIPTOR.message_types_by_name["PosixAccount"] = _POSIXACCOUNT
DESCRIPTOR.message_types_by_name["SshPublicKey"] = _SSHPUBLICKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PosixAccount = _reflection.GeneratedProtocolMessageType(
    "PosixAccount",
    (_message.Message,),
    dict(
        DESCRIPTOR=_POSIXACCOUNT,
        __module__="google.cloud.oslogin.common.common_pb2",
        __doc__="""The POSIX account information associated with a Google account.
  
  
  Attributes:
      primary:
          Only one POSIX account can be marked as primary.
      username:
          The username of the POSIX account.
      uid:
          The user ID.
      gid:
          The default group ID.
      home_directory:
          The path to the home directory for this account.
      shell:
          The path to the logic shell for this account.
      gecos:
          The GECOS (user information) entry for this account.
      system_id:
          System identifier for which account the username or uid
          applies to. By default, the empty value is used.
      account_id:
          Output only. A POSIX account identifier.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.oslogin.common.PosixAccount)
    ),
)
_sym_db.RegisterMessage(PosixAccount)

SshPublicKey = _reflection.GeneratedProtocolMessageType(
    "SshPublicKey",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SSHPUBLICKEY,
        __module__="google.cloud.oslogin.common.common_pb2",
        __doc__="""The SSH public key information associated with a Google account.
  
  
  Attributes:
      key:
          Public key text in SSH format, defined by RFC4253 section 6.6.
      expiration_time_usec:
          An expiration time in microseconds since epoch.
      fingerprint:
          Output only. The SHA-256 fingerprint of the SSH public key.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.oslogin.common.SshPublicKey)
    ),
)
_sym_db.RegisterMessage(SshPublicKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
