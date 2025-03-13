# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from course.models import Cources

class Trainee(models.Model):
    id = models.BigAutoField(primary_key=True)
    username_field = models.CharField(db_column='username ', max_length=100)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    email = models.CharField(max_length=100)
    password = models.BigIntegerField()
    cid = models.ForeignKey(Cources, models.DO_NOTHING, db_column='cid')

    class Meta:
        managed = False
        db_table = 'trainee'

    def __str__(self):
        return self.username_field