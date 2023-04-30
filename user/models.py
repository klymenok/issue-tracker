from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(DjangoUser):
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user'

    @property
    def resolved_issues(self):
        return self.issues_resolved.count()

    def created_issues(self):
        return self.issues_created.count()

