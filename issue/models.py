from django.db import models


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    created_by = models.ForeignKey(
        'user.User',
        related_name='issues_created',
        on_delete=models.DO_NOTHING,
    )
    resolved_by = models.ForeignKey(
        'user.User',
        related_name='issues_resolved',
        on_delete=models.DO_NOTHING,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        db_table = 'issue'
