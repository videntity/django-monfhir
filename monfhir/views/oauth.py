from __future__ import absolute_import
from __future__ import unicode_literals
from oauth2_provider.decorators import protected_resource
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .create import create
from .update import update
from .delete import delete
from .read import read
from apps.dot_ext.decorators import capability_protected_resource


@require_POST
@capability_protected_resource()
def oauth_create(request, resource_type):
    if request.method == "POST":
        return create(request, resource_type)
    return HttpResponse(status=501)


@capability_protected_resource()
def oauth_read_or_update_or_delete(request, resource_type, id):
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
    return kickout_400(msg)


@capability_protected_resource()
def oauth_view(request, resource_type):
    if request.method == "GET":
        return read(request, resource_type)
    return HttpResponse(status=501)
