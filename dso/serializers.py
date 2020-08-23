from rest_framework import serializers
from .models import *


class relationsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = relations
        fields = ('url','id','relation_hindi','relation_english','relation_type','relation_subtype','relation_link','relation_desc','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    def get_url(self, obj):
        return obj.get_api_url()

class relationDescSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = relation_desc
        fields = ('url','id','relation','relation_type','relation_subtype','relation_link','relation_desc','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
    
    def get_url(self, obj):
        return obj.get_api_url()

class relationHierarchySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = relation_hierarchy
        fields = ('url','id','l1_relation','l2_relation','l3_relation','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
    
    def get_url(self, obj):
        return obj.get_api_url()