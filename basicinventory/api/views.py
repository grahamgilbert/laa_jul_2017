# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from inventory.models import Machine
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from serializers import MachineSerializer


class MachineDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a machine.
    """
    queryset = Machine.objects.all()
    lookup_field = 'serial'
    serializer_class = MachineSerializer
    renderer_classes = (JSONRenderer, )
