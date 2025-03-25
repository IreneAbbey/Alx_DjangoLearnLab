from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey('accounts.CustomUser', on_delete= models.CASCADE, related_name="received_notifications")
    actor = models.ForeignKey('accounts.CustomUser', on_delete= models.CASCADE, related_name="sent_notifications")
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("target_content_type", "target_object_id")
    verb = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)