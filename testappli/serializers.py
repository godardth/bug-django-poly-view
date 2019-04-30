# PYTHON
# DJANGO
# DJANGO (THIRD PARTIES)
from rest_framework import serializers
# FULLPLANNER
from testappli.models import *

exclude_fields = ('polymorphic_ctype', 'lft', 'rght', 'tree_id')


# PUBLIC SERIALIZERS (USED BY VIEWS)

class ParentSerializer(serializers.ModelSerializer):
    cls = serializers.CharField()

    class Meta:
        model = Parent


class ChildSerializer(ParentSerializer):
    class Meta:
        model = Child
        exclude = exclude_fields
