from rest_framework import serializers
from .models import Recipient


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['first_name', 'last_name', 'apartment', 'phone_number', 'send_date', 'send_time']
