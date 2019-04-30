from django.db import models
from polymorphic_tree.models import PolymorphicMPTTModel


# BASE
class Parent(PolymorphicMPTTModel):
    role = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        pass


class Child(Parent):
    class Meta:
        proxy = True
