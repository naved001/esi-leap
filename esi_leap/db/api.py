from oslo_config import cfg
from oslo_db import api as db_api
from oslo_db import options as db_options
from oslo_log import log as logging


_BACKEND_MAPPING = {
    'sqlalchemy': 'esi_leap.db.sqlalchemy.api',
}

db_options.set_defaults(cfg.CONF)
IMPL = db_api.DBAPI(cfg.CONF.database.backend,
                    backend_mapping=_BACKEND_MAPPING)
LOG = logging.getLogger(__name__)


def get_instance():
    """Return a DB API instance."""
    return IMPL


def setup_db():
    """Set up database, create tables, etc.

    Return True on success, False otherwise
    """
    return IMPL.setup_db()


def drop_db():
    """Drop database.

    Return True on success, False otherwise
    """
    return IMPL.drop_db()


# Helpers for building constraints / equality checks


def constraint(**conditions):
    """Return a constraint object suitable for use with some updates."""
    return IMPL.constraint(**conditions)


def equal_any(*values):
    """Return an equality condition object suitable for use in a constraint.

    Equal_any conditions require that a model object's attribute equal any
    one of the given values.
    """
    return IMPL.equal_any(*values)


def not_equal(*values):
    """Return an inequality condition object suitable for use in a constraint.

    Not_equal conditions require that a model object's attribute differs from
    all of the given values.
    """
    return IMPL.not_equal(*values)


def to_dict(func):
    def decorator(*args, **kwargs):
        res = func(*args, **kwargs)

        if isinstance(res, list):
            return [item.to_dict() for item in res]

        if res:
            return res.to_dict()
        else:
            return None

    return decorator


# Policy
@to_dict
def policy_get(context, policy_uuid):
    return IMPL.policy_get(context, policy_uuid)


@to_dict
def policy_get_all(context):
    return IMPL.policy_get_all(context)


@to_dict
def policy_get_all_by_project_id(context, project_id):
    return IMPL.policy_get_all_by_project_id(context, project_id)


def policy_create(context, values):
    return IMPL.policy_create(context, values)


def policy_update(context, policy_uuid, values):
    return IMPL.policy_update(context, policy_uuid, values)


def policy_destroy(context, policy_uuid):
    IMPL.policy_destroy(context, policy_uuid)


# Applied Policy
@to_dict
def applied_policy_get(context, node_uuid, policy_uuid):
    return IMPL.applied_policy_get(context, node_uuid, policy_uuid)


@to_dict
def applied_policy_get_all(context):
    return IMPL.applied_policy_get_all(context)


@to_dict
def applied_policy_get_all_by_project_id(context, project_id):
    return IMPL.applied_policy_get_all_by_project_id(context, project_id)


def applied_policy_create(context, values):
    return IMPL.applied_policy_create(context, values)


def applied_policy_update(context, node_uuid, policy_uuid, values):
    return IMPL.applied_policy_update(context, node_uuid, policy_uuid, values)


def applied_policy_destroy(context, node_uuid, policy_uuid):
    IMPL.applied_policy_destroy(context, node_uuid, policy_uuid)


# Lease Request
@to_dict
def lease_request_get(context, request_uuid):
    return IMPL.lease_request_get(context, request_uuid)


@to_dict
def lease_request_get_all(context):
    return IMPL.lease_request_get_all(context)


@to_dict
def lease_request_get_all_by_project_id(context, project_id):
    return IMPL.lease_request_get_all_by_project_id(context, project_id)


def lease_request_create(context, values):
    return IMPL.lease_request_create(context, values)


def lease_request_update(context, request_uuid, values):
    return IMPL.lease_request_update(context, request_uuid, values)


def lease_request_destroy(context, request_uuid):
    return IMPL.lease_request_destroy(context, request_uuid)


# Leased Node
@to_dict
def leased_node_get(context, node_uuid):
    return IMPL.leased_node_get(context, node_uuid)


@to_dict
def leased_node_get_all(context):
    return IMPL.leased_node_get_all(context)


@to_dict
def leased_node_get_all_by_request_uuid(context, request_uuid):
    return IMPL.leased_node_get_all_by_request_uuid(context, request_uuid)


@to_dict
def leased_node_get_all_by_project_id(context, project_id):
    return IMPL.leased_node_get_all_by_project_id(context, project_id)


def leased_node_create(context, values):
    return IMPL.leased_node_create(context, values)


def leased_node_update(context, node_uuid, values):
    return IMPL.leased_node_update(context, node_uuid, values)


def leased_node_destroy(context, node_uuid):
    IMPL.leased_node_destroy(context, node_uuid)