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


def test_bigtable_row_data_cells():
    # [START bigtable_mutate_rows]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_keys = [b'row_key_1', b'row_key_2', b'row_key_3', b'row_key_4',
                b'row_key_20', b'row_key_22', b'row_key_200']
    rows = []
    for i, row_key in enumerate(row_keys):
        value = 'value_{}'.format(i).encode()
        row = table.row(row_key)
        row.set_cell(COLUMN_FAMILY_ID1,
                     COL_NAME1,
                     value,
                     timestamp=datetime.datetime.utcnow())
        rows.append(row)
    response = table.mutate_rows(rows)
    # validate that all rows written successfully
    for i, status in enumerate(response):
        if status.code is not 0:
            print('Row number {} failed to write'.format(i))
    # [END bigtable_mutate_rows]
    assert len(response) == len(rows)
    # [START bigtable_read_row]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = 'row_key_1'
    row = table.read_row(row_key)
    # [END bigtable_read_row]
    assert row.row_key.decode('utf-8') == row_key
    
    # [START bigtable_row_data_cells]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = 'row_key_1'
    row = table.read_row(row_key)

    cells = row.cells
    # [END bigtable_row_data_cells]
    
    actual_cell_value = cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value
    assert  actual_cell_value == b'value_0'
    
    assert row.cell_value(COLUMN_FAMILY_ID1, COL_NAME1) ==  b'value_0'

    # [START bigtable_read_rows]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    # Read full table
    partial_rows = table.read_rows()
    read_rows = [row for row in partial_rows]
    # [END bigtable_read_rows]

    assert len(read_rows) == len(rows)
    # [START bigtable_drop_by_prefix]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key_prefix = b'row_key_2'
    table.drop_by_prefix(row_key_prefix, timeout=200)
    # [END bigtable_drop_by_prefix]
    dropped_row_keys = [b'row_key_2', b'row_key_20',
                        b'row_key_22', b'row_key_200']
    for row in table.read_rows():
        assert row.row_key.decode('utf-8') not in dropped_row_keys

    # [START bigtable_truncate_table]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    table.truncate(timeout=200)
    # [END bigtable_truncate_table]
    rows_data_after_truncate = []
    for row in table.read_rows():
        rows_data_after_truncate.append(row.row_key)
    assert rows_data_after_truncate == []


def test_bigtable_row_data_cells_cell_value_cell_values():

    value = b'value_in_col1'
    row = Config.TABLE.row('row_key_1')
    row.set_cell(COLUMN_FAMILY_ID1,
                 COL_NAME1,
                 value,
                 timestamp=datetime.datetime.utcnow())
    row.commit()

    row.set_cell(COLUMN_FAMILY_ID1,
                 COL_NAME1,
                 value,
                 timestamp=datetime.datetime.utcnow())
    row.commit()

    # [START bigtable_row_data_cells]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = 'row_key_1'
    row_data = table.read_row(row_key)

    cells = row_data.cells
    # [END bigtable_row_data_cells]

    actual_cell_value = cells[COLUMN_FAMILY_ID1][COL_NAME1][0].value
    assert  actual_cell_value == value

    # [START bigtable_row_cell_value]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = 'row_key_1'
    row_data = table.read_row(row_key)

    cell_value = row_data.cell_value(COLUMN_FAMILY_ID1, COL_NAME1)
    # [END bigtable_row_cell_value]
    assert cell_value ==  value
    
    # [START bigtable_row_cell_values]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = 'row_key_1'
    row_data = table.read_row(row_key)

    cell_values = row_data.cell_values(COLUMN_FAMILY_ID1, COL_NAME1)
    # [END bigtable_row_cell_values]

    for actual_value, timestamp in cell_values:
        assert actual_value ==  value

    value2 = b'value_in_col2'
    row.set_cell(COLUMN_FAMILY_ID1, COL_NAME2, value2)
    row.commit()
    
    # [START bigtable_row_find_cells]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = 'row_key_1'
    row = table.read_row(row_key)

    cells = row.find_cells(COLUMN_FAMILY_ID1, COL_NAME2)
    # [END bigtable_row_find_cells]

    assert cells[0].value ==  value2    
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
