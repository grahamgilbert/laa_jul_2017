# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Machine(models.Model):
    MODEL_CHOICES = (
        ('MacBook', 'MacBook'),
        ('MacBook Pro 2017', 'MacBook Pro 2017'),
        ('FatMacBook Pro', 'FatMacBook Pro'),
    )

    STATUS_CHOICES = (
        ('Stock', 'Stock'),
        ('Deployed', 'Deployed'),
        ('High Risk Location', 'High Risk Location'),
        ('Lost / Stolen', 'Lost / Stolen'),
    )

    asset_number = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200, blank=True, null=True)
    serial = models.CharField(max_length=200)
    created_date = models.DateTimeField(editable=False)
    modified_date = models.DateTimeField(editable=False)
    model = models.CharField(choices=MODEL_CHOICES, max_length=200)
    status = models.CharField(choices=STATUS_CHOICES, max_length=200,
                              default='Stock')
    windows_vm = models.BooleanField(default=False, verbose_name='Assign a Windows VM')
    encryption_required = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Machine, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {}'.format(self.asset_number, self.serial)
