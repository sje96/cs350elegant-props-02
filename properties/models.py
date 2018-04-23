# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Property(models.Model):
    prop_type = models.CharField(max_length=48)
    picture_url = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    nearest_elementary = models.CharField(max_length=256)
    street = models.CharField(max_length=255, null=True)    
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2, null=True)
    zip_code = models.IntegerField(default=87701, null=True)

    def __str__(self):
        return self.prop_type + ' @ ' + str(self.street)



