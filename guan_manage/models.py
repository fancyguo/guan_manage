# coding=utf-8

from django.db import models
from utils import tools


class Base(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

    def __str__(self):
        if 'name' in self:
            return self.name
        else:
            return self.id

    def remove(self):
        # soft remove
        self.deleted = True
        self.updated_at = tools.utc_now()
        self.save()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, is_clean=None):
        if not is_clean:
            self.updated_at = tools.utc_now()
        if not self.created_at:
            self.created_at = tools.utc_now()
        super(Base, self).save(force_insert=force_insert,
                               force_update=force_update, using=using)
