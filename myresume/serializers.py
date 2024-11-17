from rest_framework import serializers
from .models import myresume

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = myresume
        fields = "__all__"