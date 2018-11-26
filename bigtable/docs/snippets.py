#!/usr/bin/env python

# Copyright 2018, Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Testable usage examples for Google Cloud Bigtable API wrapper

Each example function takes a ``client`` argument (which must be an instance
of :class:`google.cloud.bigtable.client.Client`) and uses it to perform a task
with the API.

To facilitate running the examples as system tests, each example is also passed
a ``to_delete`` list;  the function adds to the list any objects created which
need to be deleted during teardown.

.. note::
    This file is under progress and will be updated with more guidance from
    the team. Unit tests will be added with guidance from the team.

"""

import datetime
import pytest

from test_utils.system import unique_resource_id
from google.cloud._helpers import UTC
from google.cloud.bigtable import Client
from google.cloud.bigtable import enums
from google.cloud.bigtable import column_family


INSTANCE_ID = "snippet" + unique_resource_id('-')
CLUSTER_ID = "clus-1" + unique_resource_id('-')
TABLE_ID = "tabl-1" + unique_resource_id('-')
LOCATION_ID = 'us-central1-f'
ALT_LOCATION_ID = 'us-central1-a'
PRODUCTION = enums.Instance.Type.PRODUCTION
SERVER_NODES = 3
STORAGE_TYPE = enums.StorageType.SSD
LABEL_KEY = u'python-snippet'
LABEL_STAMP = datetime.datetime.utcnow() \
                               .replace(microsecond=0, tzinfo=UTC,) \
                               .strftime("%Y-%m-%dt%H-%M-%S")
LABELS = {LABEL_KEY: str(LABEL_STAMP)}
COLUMN_FAMILY_ID1 = "col_fam_id1"
COL_NAME1 = b'col-name1'
CELL_VAL1 = b'cell-val1'
ROW_KEY1 = b'row_key_id1'
COLUMN_FAMILY_ID2 = "col_fam_id2"
COL_NAME2 = b'col-name2'
CELL_VAL2 = b'cell-val2'
ROW_KEY2 = b'row_key_id2'


class Config(object):
    """Run-time configuration to be modified at set-up.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """
    CLIENT = None
    INSTANCE = None
    TABLE = None


def setup_module():
    client = Config.CLIENT = Client(admin=True)
    Config.INSTANCE = client.instance(INSTANCE_ID,
                                      instance_type=PRODUCTION,
                                      labels=LABELS)
    cluster = Config.INSTANCE.cluster(CLUSTER_ID,
                                      location_id=LOCATION_ID,
                                      serve_nodes=SERVER_NODES,
                                      default_storage_type=STORAGE_TYPE)
    operation = Config.INSTANCE.create(clusters=[cluster])
    # We want to make sure the operation completes.
    operation.result(timeout=100)


def teardown_module():
    Config.INSTANCE.delete()


def test_bigtable_create_instance():
    # [START bigtable_create_prod_instance]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable import enums

    my_instance_id = "inst-my-" + unique_resource_id('-')
    my_cluster_id = "clus-my-" + unique_resource_id('-')
    location_id = 'us-central1-f'
    serve_nodes = 3
    storage_type = enums.StorageType.SSD
    production = enums.Instance.Type.PRODUCTION
    labels = {'prod-label': 'prod-label'}

    client = Client(admin=True)
    instance = client.instance(my_instance_id, instance_type=production,
                               labels=labels)
    cluster = instance.cluster(my_cluster_id, location_id=location_id,
                               serve_nodes=serve_nodes,
                               default_storage_type=storage_type)
    operation = instance.create(clusters=[cluster])
    # We want to make sure the operation completes.
    operation.result(timeout=100)
    # [END bigtable_create_prod_instance]
    assert instance.exists()
    instance.delete()


def test_bigtable_create_additional_cluster():
    # [START bigtable_create_cluster]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable import enums

    # Assuming that there is an existing instance with `INSTANCE_ID`
    # on the server already.
    # to create an instance see
    # 'https://cloud.google.com/bigtable/docs/creating-instance'

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)

    cluster_id = "clus-my-" + unique_resource_id('-')
    location_id = 'us-central1-a'
    serve_nodes = 3
    storage_type = enums.StorageType.SSD

    cluster = instance.cluster(cluster_id, location_id=location_id,
                               serve_nodes=serve_nodes,
                               default_storage_type=storage_type)
    operation = cluster.create()
    # We want to make sure the operation completes.
    operation.result(timeout=100)
    # [END bigtable_create_cluster]
    assert cluster.exists()

    cluster.delete()


def test_bigtable_create_app_profile():
    # [START bigtable_create_app_profile]
    from google.cloud.bigtable import Client
    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)

    app_profile_id = "app-prof-" + unique_resource_id('-')
    description = 'routing policy-multy'
    routing_policy_type = enums.RoutingPolicyType.ANY

    app_profile = instance.app_profile(
        app_profile_id=app_profile_id,
        routing_policy_type=routing_policy_type,
        description=description,
        cluster_id=CLUSTER_ID)

    app_profile = app_profile.create(ignore_warnings=True)
    # [END bigtable_create_app_profile]
    assert app_profile.exists()

    app_profile.delete(ignore_warnings=True)


def test_bigtable_batcher_mutate_flush_mutate_rows():
    # [START bigtable_batcher_mutate]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    # Batcher for max row bytes, max_row_bytes=1024 is optional.
    batcher = table.mutations_batcher(max_row_bytes=1024)

    # Add a single row
    row_key = b'row_key_1'
    row = table.row(row_key)
    row.set_cell(COLUMN_FAMILY_ID1,
                 COL_NAME1,
                 'value-0',
                 timestamp=datetime.datetime.utcnow())

    # In batcher, mutate will flush current batch if it
    # reaches the max_row_bytes
    batcher.mutate(row)
    batcher.flush()
    # [END bigtable_batcher_mutate]
    
    # [START bigtable_batcher_flush]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    # Batcher for max row bytes, max_row_bytes=1024 is optional.
    batcher = table.mutations_batcher(max_row_bytes=1024)

    # Add a single row
    row_key = b'row_key'
    row = table.row(row_key)
    row.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, 'value-0')

    # In batcher, mutate will flush current batch if it
    # reaches the max_row_bytes
    batcher.mutate(row)
    batcher.flush()
    # [END bigtable_batcher_flush]

    rows_on_table = []
    for row in table.read_rows():
        rows_on_table.append(row.row_key)
    assert len(rows_on_table) == 2
    table.truncate(timeout=200)

    # [START bigtable_batcher_mutate_rows]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    batcher = table.mutations_batcher()
    
    row1 = table.row(b'row_key_1')
    row2 = table.row(b'row_key_2')
    row3 = table.row(b'row_key_3')
    row4 = table.row(b'row_key_4')

    row1.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, b'cell-val1')
    row2.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, b'cell-val2')
    row3.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, b'cell-val3')
    row4.set_cell(COLUMN_FAMILY_ID1, COL_NAME1, b'cell-val4')

    batcher.mutate_rows([row1, row2, row3, row4])

    # batcher will flush current batch if it
    # reaches the max flush_count
    # Manually send the current batch to Cloud Bigtable
    batcher.flush()
    # [END bigtable_batcher_mutate_rows]

    rows_on_table = []
    for row in table.read_rows():
        rows_on_table.append(row.row_key)
    assert len(rows_on_table) == 4
    table.truncate(timeout=200)


def test_bigtable_list_instances():
    # [START bigtable_list_instances]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    (instances_list, failed_locations_list) = client.list_instances()
    # [END bigtable_list_instances]
    assert len(instances_list) > 0


def test_bigtable_list_clusters_on_instance():
    # [START bigtable_list_clusters_on_instance]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    (clusters_list, failed_locations_list) = instance.list_clusters()
    # [END bigtable_list_clusters_on_instance]
    assert len(clusters_list) > 0


def test_bigtable_list_clusters_in_project():
    # [START bigtable_list_clusters_in_project]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    (clusters_list, failed_locations_list) = client.list_clusters()
    # [END bigtable_list_clusters_in_project]
    assert len(clusters_list) > 0


def test_bigtable_list_app_profiles():
    # [START bigtable_list_app_profiles]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    # [END bigtable_list_app_profiles]

    app_profile = instance.app_profile(
        app_profile_id="app-prof-" + unique_resource_id('-'),
        routing_policy_type=enums.RoutingPolicyType.ANY)
    app_profile = app_profile.create(ignore_warnings=True)

    # [START bigtable_list_app_profiles]
    app_profiles_list = instance.list_app_profiles()
    # [END bigtable_list_app_profiles]
    assert len(app_profiles_list) > 0


def test_bigtable_instance_exists():
    # [START bigtable_check_instance_exists]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    instance_exists = instance.exists()
    # [END bigtable_check_instance_exists]
    assert instance_exists


def test_bigtable_cluster_exists():
    # [START bigtable_check_cluster_exists]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    cluster = instance.cluster(CLUSTER_ID)
    cluster_exists = cluster.exists()
    # [END bigtable_check_cluster_exists]
    assert cluster_exists


def test_bigtable_reload_instance():
    # [START bigtable_reload_instance]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    instance.reload()
    # [END bigtable_reload_instance]
    assert instance.type_ == PRODUCTION.value


def test_bigtable_reload_cluster():
    # [START bigtable_reload_cluster]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    cluster = instance.cluster(CLUSTER_ID)
    cluster.reload()
    # [END bigtable_reload_cluster]
    assert cluster.serve_nodes == SERVER_NODES


def test_bigtable_update_instance():
    # [START bigtable_update_instance]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    display_name = "My new instance"
    instance.display_name = display_name
    instance.update()
    # [END bigtable_update_instance]
    assert instance.display_name == display_name


def test_bigtable_update_cluster():
    # [START bigtable_update_cluster]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    cluster = instance.cluster(CLUSTER_ID)
    cluster.serve_nodes = 4
    cluster.update()
    # [END bigtable_update_cluster]
    assert cluster.serve_nodes == 4


def test_bigtable_create_table():
    # [START bigtable_create_table]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable import column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table("table_my")
    # Define the GC policy to retain only the most recent 2 versions.
    max_versions_rule = column_family.MaxVersionsGCRule(2)
    table.create(column_families={'cf1': max_versions_rule})
    # [END bigtable_create_table]
    assert table.exists()


def test_bigtable_list_tables():
    # [START bigtable_list_tables]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    tables_list = instance.list_tables()
    # [END bigtable_list_tables]
    assert len(tables_list) > 0


def test_bigtable_delete_cluster():
    # [START bigtable_delete_cluster]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    cluster_id = "clus-my-" + unique_resource_id('-')
    # [END bigtable_delete_cluster]

    cluster = instance.cluster(cluster_id, location_id=ALT_LOCATION_ID,
                               serve_nodes=SERVER_NODES,
                               default_storage_type=STORAGE_TYPE)
    operation = cluster.create()
    # We want to make sure the operation completes.
    operation.result(timeout=1000)

    # [START bigtable_delete_cluster]
    cluster_to_delete = instance.cluster(cluster_id)
    cluster_to_delete.delete()
    # [END bigtable_delete_cluster]
    assert not cluster_to_delete.exists()


def test_bigtable_delete_instance():
    # [START bigtable_delete_instance]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance_id_to_delete = "inst-my-" + unique_resource_id('-')
    # [END bigtable_delete_instance]

    cluster_id = "clus-my-" + unique_resource_id('-')

    instance = client.instance(instance_id_to_delete,
                               instance_type=PRODUCTION,
                               labels=LABELS)
    cluster = instance.cluster(cluster_id,
                               location_id=ALT_LOCATION_ID,
                               serve_nodes=SERVER_NODES,
                               default_storage_type=STORAGE_TYPE)
    operation = instance.create(clusters=[cluster])
    # We want to make sure the operation completes.
    operation.result(timeout=100)

    # [START bigtable_delete_instance]
    instance_to_delete = client.instance(instance_id_to_delete)
    instance_to_delete.delete()
    # [END bigtable_delete_instance]

    assert not instance_to_delete.exists()


def test_bigtable_test_iam_permissions():
    # [START bigtable_test_iam_permissions]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    instance.reload()
    permissions = ["bigtable.clusters.create", "bigtable.tables.create"]
    permissions_allowed = instance.test_iam_permissions(permissions)
    # [END bigtable_test_iam_permissions]

    assert permissions_allowed == permissions


def test_bigtable_set_iam_policy_then_get_iam_policy():
    # [START bigtable_set_iam_policy]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable.policy import Policy
    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE

    # [END bigtable_set_iam_policy]

    service_account_email = Config.CLIENT._credentials.service_account_email

    # [START bigtable_set_iam_policy]
    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    instance.reload()
    new_policy = Policy()
    new_policy[BIGTABLE_ADMIN_ROLE] = [
        Policy.service_account(service_account_email),
    ]

    policy_latest = instance.set_iam_policy(new_policy)
    # [END bigtable_set_iam_policy]

    assert len(policy_latest.bigtable_admins) > 0

    # [START bigtable_get_iam_policy]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    policy = instance.get_iam_policy()
    # [END bigtable_get_iam_policy]

    assert len(policy.bigtable_admins) > 0


if __name__ == '__main__':
    pytest.main()
