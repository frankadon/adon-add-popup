from django.db.models import fields
from rest_framework import serializers
from .models import CardData


class CardDataSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CardData
        fields = [
            'id',
            'title',
            # 'ref_code',
            'business_name',
            'greet',
            'promotion',
            'closing_statement',
            'image',
            'add_start_date',
            'add_end_date',
            'is_popup_active',
            'created',
            'updated'
        ]
