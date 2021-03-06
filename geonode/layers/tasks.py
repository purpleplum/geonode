# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

"""celery tasks for geonode.layers."""

from celery.app import shared_task
from celery.utils.log import get_task_logger

from geonode.layers.models import Layer

logger = get_task_logger(__name__)


@shared_task(bind=True, queue='cleanup')
def delete_layer(self, object_id):
    """
    Deletes a layer.
    """
    logger.info('Deleting Layer ID {0}'.format(object_id))
    try:
        layer = Layer.objects.get(id=object_id)
    except Layer.DoesNotExist:
        return

    layer.delete()
