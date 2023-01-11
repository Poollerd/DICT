from rest_framework import serializers

from .models import Network

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        read_only_fields = (
            'team_name',
            'created_by',
            'created_at',

        ),
  
        fields = (
            'id',
            'network_install_place',
            'network_type',
            'network_brand',
            'network_name',
            # 'network_version',
            'network_name_in_system',
            'network_mac_address',
            'network_ip_address',
            'network_got',
            'network_serial_number',
            'network_person_responsible',
            'network_person_responsible_phone',
            'network_status',
            'network_note',
            'created_at',
        )
