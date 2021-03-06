from __future__ import absolute_import
from __future__ import unicode_literals
from ..utils import operational_outcome_error
from .update import update
from .delete import delete
from .read import read
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def read_or_update_or_delete(request, resource_type, id):
    """Route to read, update, or delete based on HTTP method FHIR Interaction"""

    if request.method == 'GET':
        # Read
        return read(request, resource_type, id)
    elif request.method == 'PUT':
        # update
        return update(request, resource_type, id)
    elif request.method == 'DELETE':
        # delete
        return delete(request, resource_type, id)
    # else:
    # Not supported.
    msg = "HTTP method %s not supported at this URL." % (request.method)
    return operational_outcome_error(msg, 400)
