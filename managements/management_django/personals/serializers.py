from rest_framework import serializers

from .models import Personal

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',

        ),

        fields = (
            'id',
            'rank',
            'first_name',
            'last_name',
            'position',
            'email_rtaf',
            'email_public',
            'mobile',
            'phone_rtaf',
            'status',
            'department',
            # 'created_by',
            'created_at',
            'modified_at'
        )

