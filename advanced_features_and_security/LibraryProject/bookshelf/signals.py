from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "bookshelf":  
        editors_group, created = Group.objects.get_or_create(name="Editors")
        viewers_group, created = Group.objects.get_or_create(name="Viewers")
        admins_group, created = Group.objects.get_or_create(name="Admins")

        book_content_type = ContentType.objects.get_for_model(Book)

        can_view = Permission.objects.get(codename="can_view", content_type=book_content_type)
        can_create = Permission.objects.get(codename="can_create", content_type=book_content_type)
        can_edit = Permission.objects.get(codename="can_edit", content_type=book_content_type)
        can_delete = Permission.objects.get(codename="can_delete", content_type=book_content_type)

        editors_group.permissions.set([can_create, can_edit, can_view])
        viewers_group.permissions.set([can_view])
        admins_group.permissions.set([can_create, can_edit, can_delete, can_view])

        print("Groups and permissions created successfully!")
