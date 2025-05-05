# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField, ArrayField

from django.db import models

# Create your models here.
class Country(models.Model):
    name = JSONField(blank=False, null=False)
    tld = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    cca2 = models.CharField(max_length=100, unique=True)
    ccn3 = models.CharField(max_length=100)
    cioc2 = models.CharField(max_length=100)
    independent = models.BooleanField(default=False)
    status = models.CharField(max_length=100)
    unmember = models.BooleanField(default=False)
    currencies = JSONField(blank=True, null=True)
    idd = JSONField(blank=True, null=True)
    capital = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    altSpellings = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    subregion = models.CharField(max_length=30, blank=True, null=True)
    languages =  JSONField(blank=True, null=True)
    latlng = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    landlocked = models.BooleanField(default=False)
    borders = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    area = models.BigIntegerField()
    demonyms = JSONField(blank=True, null=True)
    cca3 = models.CharField(max_length=100)
    translations = JSONField(blank=True, null=True)
    flag = models.CharField(max_length=100, blank=True, null=True)
    maps = JSONField(blank=True, null=True)
    population = models.BigIntegerField()
    gini = JSONField(blank=True, null=True)
    fifa = models.CharField(max_length=10, blank=True, null=True)
    car = JSONField(blank=True, null=True)
    timezones = JSONField(blank=True, null=True)
    continents = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    flags = JSONField(blank=True, null=True)
    coatOfArms = JSONField(blank=True, null=True)
    startOfWeek = models.CharField(max_length=20, blank=True, null=True)
    capitalInfo = JSONField(blank=True, null=True)
    postalCode = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['cca2']
