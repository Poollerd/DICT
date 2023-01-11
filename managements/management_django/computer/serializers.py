from rest_framework import serializers

from .models import Computer, Upgradecomputer

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        read_only_fields = (
            'team_name',
            'created_by',
            'created_at',

        ),

        fields = (
            'id',
            'computer_install_place',
            'computer_type',
            'computer_name',
            'computer_brand',
            'computer_series',
            'computer_number_rtaf',
            'computer_series_number',
            'cpu_brand',
            'cpu_model',
            'cpu_speed_clock',
            'cpu_unit_speed_clock',
            'computer_mac_address',
            'computer_use_network',
            'ram_type',
            'ram_capacity',
            'ram_unit_capacity',
            'harddisk_type_1',
            'harddisk_capacity_1',
            'harddisk_unit_1',
            'harddisk_type_2',
            'harddisk_capacity_2',
            'harddisk_unit_2',
            'os_computer',
            'os_copyright',
            'office_name',
            'office_model_year',
            'office_copyright',
            'antivirus_name',
            'antivirus_copyright',
            'computer_acquisition',
            'computer_start_use_year',
            'person_responsible',
            'person_responsible_phone',
            'status_computer',
            'note',
            # 'created_by',
            'created_at',
        )

class UpgradecomputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgradecomputer
        fields = (
            'id',
            'computer_install_place',
            'computer_name',
            'computer_upgrade_year',
            'cpu_brand',
            'cpu_model',
            'cpu_speed_clock',
            'cpu_unit_speed_clock',
            'computer_use_network',
            'ram_type',
            'ram_capacity',
            'ram_unit_capacity',
            'harddisk_type_1',
            'harddisk_capacity_1',
            'harddisk_unit_1',
            'harddisk_type_2',
            'harddisk_capacity_2',
            'harddisk_unit_2',
            'os_computer',
            'os_copyright',
            'office_name',
            'office_model_year',
            'office_copyright',
            'antivirus_name',
            'antivirus_copyright',
            'computer_upgrade_year',
            'person_responsible',
            'person_responsible_phone',
            'status_computer',
            'note',

        )
    
