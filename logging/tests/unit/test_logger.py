# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import mock


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class TestLogger(unittest.TestCase):

    PROJECT = "test-project"
    LOGGER_NAME = "logger-name"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging.logger import Logger

        return Logger

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        conn = object()
        client = _Client(self.PROJECT, conn)
        logger = self._make_one(self.LOGGER_NAME, client=client)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)
        self.assertEqual(
            logger.full_name, "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertEqual(
            logger.path, "/projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertIsNone(logger.labels)

    def test_ctor_explicit(self):
        LABELS = {"foo": "bar", "baz": "qux"}
        conn = object()
        client = _Client(self.PROJECT, conn)
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=LABELS)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)
        self.assertEqual(
            logger.full_name, "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertEqual(
            logger.path, "/projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertEqual(logger.labels, LABELS)

    def test_batch_w_bound_client(self):
        from google.cloud.logging.logger import Batch

        conn = object()
        client = _Client(self.PROJECT, conn)
        logger = self._make_one(self.LOGGER_NAME, client=client)
        batch = logger.batch()
        self.assertIsInstance(batch, Batch)
        self.assertIs(batch.logger, logger)
        self.assertIs(batch.client, client)

    def test_batch_w_alternate_client(self):
        from google.cloud.logging.logger import Batch

        conn1 = object()
        conn2 = object()
        client1 = _Client(self.PROJECT, conn1)
        client2 = _Client(self.PROJECT, conn2)
        logger = self._make_one(self.LOGGER_NAME, client=client1)
        batch = logger.batch(client2)
        self.assertIsInstance(batch, Batch)
        self.assertIs(batch.logger, logger)
        self.assertIs(batch.client, client2)

    def test_log_empty_defaults_w_default_labels(self):
        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "resource": {"type": "global", "labels": {}},
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_empty()

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_empty_w_explicit(self):
        import datetime
        from google.cloud.logging.resource import Resource

        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_empty(
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_text_defaults(self):
        TEXT = "TEXT"
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "textPayload": TEXT,
                "resource": {"type": "global", "labels": {}},
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log_text(TEXT)

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_text_w_unicode_and_default_labels(self):
        TEXT = u"TEXT"
        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "textPayload": TEXT,
                "resource": {"type": "global", "labels": {}},
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_text(TEXT)

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_text_explicit(self):
        import datetime
        from google.cloud.logging.resource import Resource

        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        TEXT = "TEXT"
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "textPayload": TEXT,
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_text(
            TEXT,
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_struct_defaults(self):
        STRUCT = {"message": "MESSAGE", "weather": "cloudy"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "jsonPayload": STRUCT,
                "resource": {"type": "global", "labels": {}},
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log_struct(STRUCT)

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_struct_w_default_labels(self):
        STRUCT = {"message": "MESSAGE", "weather": "cloudy"}
        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "jsonPayload": STRUCT,
                "resource": {"type": "global", "labels": {}},
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_struct(STRUCT)

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_struct_w_explicit(self):
        import datetime
        from google.cloud.logging.resource import Resource

        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        STRUCT = {"message": "MESSAGE", "weather": "cloudy"}
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "jsonPayload": STRUCT,
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_struct(
            STRUCT,
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_proto_defaults(self):
        import json
        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        message = Struct(fields={"foo": Value(bool_value=True)})
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "protoPayload": json.loads(MessageToJson(message)),
                "resource": {"type": "global", "labels": {}},
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log_proto(message)

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_proto_w_default_labels(self):
        import json
        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        message = Struct(fields={"foo": Value(bool_value=True)})
        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "protoPayload": json.loads(MessageToJson(message)),
                "resource": {"type": "global", "labels": {}},
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_proto(message)

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_log_proto_w_explicit(self):
        import json
        import datetime
        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct
        from google.protobuf.struct_pb2 import Value
        from google.cloud.logging.resource import Resource

        message = Struct(fields={"foo": Value(bool_value=True)})
        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "protoPayload": json.loads(MessageToJson(message)),
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_proto(
            message,
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(api._write_entries_called_with, (ENTRIES, None, None, None))

    def test_delete_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.delete()

        self.assertEqual(
            api._logger_delete_called_with, (self.PROJECT, self.LOGGER_NAME)
        )

    def test_delete_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1)

        logger.delete(client=client2)

        self.assertEqual(
            api._logger_delete_called_with, (self.PROJECT, self.LOGGER_NAME)
        )

    def test_list_entries_defaults(self):
        import six
        from google.cloud.logging.client import Client

        TOKEN = "TOKEN"

        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"nextPageToken": TOKEN}
        client._connection = _Connection(returned)

        logger = self._make_one(self.LOGGER_NAME, client=client)

        iterator = logger.list_entries()
        page = six.next(iterator.pages)
        entries = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(entries), 0)
        self.assertEqual(token, TOKEN)
        called_with = client._connection._called_with
        FILTER = "logName=projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        self.assertEqual(
            called_with,
            {
                "method": "POST",
                "path": "/entries:list",
                "data": {"filter": FILTER, "projectIds": [self.PROJECT]},
            },
        )

    def test_list_entries_explicit(self):
        from google.cloud.logging import DESCENDING
        from google.cloud.logging.client import Client

        PROJECT1 = "PROJECT1"
        PROJECT2 = "PROJECT2"
        FILTER = "resource.type:global"
        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        client._connection = _Connection({})
        logger = self._make_one(self.LOGGER_NAME, client=client)
        iterator = logger.list_entries(
            projects=[PROJECT1, PROJECT2],
            filter_=FILTER,
            order_by=DESCENDING,
            page_size=PAGE_SIZE,
            page_token=TOKEN,
        )
        entries = list(iterator)
        token = iterator.next_page_token

        self.assertEqual(len(entries), 0)
        self.assertIsNone(token)
        # self.assertEqual(client._listed, LISTED)
        called_with = client._connection._called_with
        combined_filter = "%s AND logName=projects/%s/logs/%s" % (
            FILTER,
            self.PROJECT,
            self.LOGGER_NAME,
        )
        self.assertEqual(
            called_with,
            {
                "method": "POST",
                "path": "/entries:list",
                "data": {
                    "filter": combined_filter,
                    "orderBy": DESCENDING,
                    "pageSize": PAGE_SIZE,
                    "pageToken": TOKEN,
                    "projectIds": [PROJECT1, PROJECT2],
                },
            },
        )


class TestBatch(unittest.TestCase):

    PROJECT = "test-project"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging.logger import Batch

        return Batch

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_ctor_defaults(self):
        logger = _Logger()
        client = _Client(project=self.PROJECT)
        batch = self._make_one(logger, client)
        self.assertIs(batch.logger, logger)
        self.assertIs(batch.client, client)
        self.assertEqual(len(batch.entries), 0)

    def test_log_empty_defaults(self):
        from google.cloud.logging.entries import LogEntry

        ENTRY = LogEntry()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_empty()
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_empty_explicit(self):
        import datetime
        from google.cloud.logging.resource import Resource
        from google.cloud.logging.entries import LogEntry

        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        ENTRY = LogEntry(
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_empty(
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_text_defaults(self):
        from google.cloud.logging.entries import _GLOBAL_RESOURCE
        from google.cloud.logging.entries import TextEntry

        TEXT = "This is the entry text"
        ENTRY = TextEntry(payload=TEXT, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_text(TEXT)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_text_explicit(self):
        import datetime
        from google.cloud.logging.resource import Resource
        from google.cloud.logging.entries import TextEntry

        TEXT = "This is the entry text"
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        ENTRY = TextEntry(
            payload=TEXT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_text(
            TEXT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_struct_defaults(self):
        from google.cloud.logging.entries import _GLOBAL_RESOURCE
        from google.cloud.logging.entries import StructEntry

        STRUCT = {"message": "Message text", "weather": "partly cloudy"}
        ENTRY = StructEntry(payload=STRUCT, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_struct(STRUCT)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_struct_explicit(self):
        import datetime
        from google.cloud.logging.resource import Resource
        from google.cloud.logging.entries import StructEntry

        STRUCT = {"message": "Message text", "weather": "partly cloudy"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRY = StructEntry(
            payload=STRUCT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_struct(
            STRUCT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_proto_defaults(self):
        from google.cloud.logging.entries import _GLOBAL_RESOURCE
        from google.cloud.logging.entries import ProtobufEntry
        from google.protobuf.struct_pb2 import Struct
        from google.protobuf.struct_pb2 import Value

        message = Struct(fields={"foo": Value(bool_value=True)})
        ENTRY = ProtobufEntry(payload=message, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_proto(message)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_proto_explicit(self):
        import datetime
        from google.cloud.logging.resource import Resource
        from google.cloud.logging.entries import ProtobufEntry
        from google.protobuf.struct_pb2 import Struct
        from google.protobuf.struct_pb2 import Value

        message = Struct(fields={"foo": Value(bool_value=True)})
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRY = ProtobufEntry(
            payload=message,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_proto(
            message,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_commit_w_unknown_entry_type(self):
        from google.cloud.logging.entries import _GLOBAL_RESOURCE
        from google.cloud.logging.entries import LogEntry

        logger = _Logger()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        api = client.logging_api = _DummyLoggingAPI()
        batch = self._make_one(logger, client)
        batch.entries.append(LogEntry(severity="blah"))
        ENTRY = {"severity": "blah", "resource": _GLOBAL_RESOURCE._to_dict()}

        batch.commit()

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with, ([ENTRY], logger.full_name, None, None)
        )

    def test_commit_w_resource_specified(self):
        from google.cloud.logging.entries import _GLOBAL_RESOURCE
        from google.cloud.logging.resource import Resource

        logger = _Logger()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        api = client.logging_api = _DummyLoggingAPI()
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )

        batch = self._make_one(logger, client, resource=RESOURCE)
        MESSAGE = "This is the entry text"
        ENTRIES = [
            {"textPayload": MESSAGE},
            {"textPayload": MESSAGE, "resource": _GLOBAL_RESOURCE._to_dict()},
        ]
        batch.log_text(MESSAGE, resource=None)
        batch.log_text(MESSAGE)
        batch.commit()
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, RESOURCE._to_dict(), None),
        )

    def test_commit_w_bound_client(self):
        import json
        import datetime
        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct
        from google.protobuf.struct_pb2 import Value
        from google.cloud._helpers import _datetime_to_rfc3339
        from google.cloud.logging.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        message = Struct(fields={"foo": Value(bool_value=True)})
        IID1 = "IID1"
        IID2 = "IID2"
        IID3 = "IID3"
        TIMESTAMP1 = datetime.datetime(2016, 12, 31, 0, 0, 1, 999999)
        TIMESTAMP2 = datetime.datetime(2016, 12, 31, 0, 0, 2, 999999)
        TIMESTAMP3 = datetime.datetime(2016, 12, 31, 0, 0, 3, 999999)
        TRACE1 = "12345678-1234-5678-1234-567812345678"
        TRACE2 = "12345678-1234-5678-1234-567812345679"
        TRACE3 = "12345678-1234-5678-1234-567812345670"
        SPANID1 = "000000000000004a"
        SPANID2 = "000000000000004b"
        SPANID3 = "000000000000004c"
        ENTRIES = [
            {
                "textPayload": TEXT,
                "insertId": IID1,
                "timestamp": _datetime_to_rfc3339(TIMESTAMP1),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "trace": TRACE1,
                "spanId": SPANID1,
                "traceSampled": True,
            },
            {
                "jsonPayload": STRUCT,
                "insertId": IID2,
                "timestamp": _datetime_to_rfc3339(TIMESTAMP2),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "trace": TRACE2,
                "spanId": SPANID2,
                "traceSampled": False,
            },
            {
                "protoPayload": json.loads(MessageToJson(message)),
                "insertId": IID3,
                "timestamp": _datetime_to_rfc3339(TIMESTAMP3),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "trace": TRACE3,
                "spanId": SPANID3,
                "traceSampled": True,
            },
        ]
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = _Logger()
        batch = self._make_one(logger, client=client)

        batch.log_text(
            TEXT,
            insert_id=IID1,
            timestamp=TIMESTAMP1,
            trace=TRACE1,
            span_id=SPANID1,
            trace_sampled=True,
        )
        batch.log_struct(
            STRUCT,
            insert_id=IID2,
            timestamp=TIMESTAMP2,
            trace=TRACE2,
            span_id=SPANID2,
            trace_sampled=False,
        )
        batch.log_proto(
            message,
            insert_id=IID3,
            timestamp=TIMESTAMP3,
            trace=TRACE3,
            span_id=SPANID3,
            trace_sampled=True,
        )
        batch.commit()

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, logger.full_name, None, None)
        )

    def test_commit_w_alternate_client(self):
        import json
        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct
        from google.protobuf.struct_pb2 import Value
        from google.cloud.logging.logger import Logger
        from google.cloud.logging.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        message = Struct(fields={"foo": Value(bool_value=True)})
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = Logger("logger_name", client1, labels=DEFAULT_LABELS)
        ENTRIES = [
            {
                "textPayload": TEXT,
                "labels": LABELS,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "jsonPayload": STRUCT,
                "severity": SEVERITY,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "protoPayload": json.loads(MessageToJson(message)),
                "httpRequest": REQUEST,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
        ]
        batch = self._make_one(logger, client=client1)

        batch.log_text(TEXT, labels=LABELS)
        batch.log_struct(STRUCT, severity=SEVERITY)
        batch.log_proto(message, http_request=REQUEST)
        batch.commit(client=client2)

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, None, DEFAULT_LABELS),
        )

    def test_context_mgr_success(self):
        import json
        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct
        from google.protobuf.struct_pb2 import Value
        from google.cloud.logging.logger import Logger
        from google.cloud.logging.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        message = Struct(fields={"foo": Value(bool_value=True)})
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = Logger("logger_name", client, labels=DEFAULT_LABELS)
        ENTRIES = [
            {
                "textPayload": TEXT,
                "httpRequest": REQUEST,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "jsonPayload": STRUCT,
                "labels": LABELS,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "protoPayload": json.loads(MessageToJson(message)),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "severity": SEVERITY,
            },
        ]
        batch = self._make_one(logger, client=client)

        with batch as other:
            other.log_text(TEXT, http_request=REQUEST)
            other.log_struct(STRUCT, labels=LABELS)
            other.log_proto(message, severity=SEVERITY)

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, None, DEFAULT_LABELS),
        )

    def test_context_mgr_failure(self):
        import datetime
        from google.protobuf.struct_pb2 import Struct
        from google.protobuf.struct_pb2 import Value
        from google.cloud.logging.entries import TextEntry
        from google.cloud.logging.entries import StructEntry
        from google.cloud.logging.entries import ProtobufEntry

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        message = Struct(fields={"foo": Value(bool_value=True)})
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = _Logger()
        UNSENT = [
            TextEntry(payload=TEXT, insert_id=IID, timestamp=TIMESTAMP),
            StructEntry(payload=STRUCT, severity=SEVERITY),
            ProtobufEntry(payload=message, labels=LABELS, http_request=REQUEST),
        ]
        batch = self._make_one(logger, client=client)

        try:
            with batch as other:
                other.log_text(TEXT, insert_id=IID, timestamp=TIMESTAMP)
                other.log_struct(STRUCT, severity=SEVERITY)
                other.log_proto(message, labels=LABELS, http_request=REQUEST)
                raise _Bugout()
        except _Bugout:
            pass

        self.assertEqual(list(batch.entries), UNSENT)
        self.assertIsNone(api._write_entries_called_with)


class _Logger(object):

    labels = None

    def __init__(self, name="NAME", project="PROJECT"):
        self.full_name = "projects/%s/logs/%s" % (project, name)


class _DummyLoggingAPI(object):

    _write_entries_called_with = None

    def write_entries(self, entries, logger_name=None, resource=None, labels=None):
        self._write_entries_called_with = (entries, logger_name, resource, labels)

    def logger_delete(self, project, logger_name):
        self._logger_delete_called_with = (project, logger_name)


class _Client(object):
    def __init__(self, project, connection=None):
        self.project = project
        self._connection = connection


class _Bugout(Exception):
    pass


class _Connection(object):

    _called_with = None

    def __init__(self, *responses):
        self._responses = responses

    def api_request(self, **kw):
        self._called_with = kw
        response, self._responses = self._responses[0], self._responses[1:]
        return response
