from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ["name", "roll_no", "id", "city"]
    
    def validate_roll_no(self, value):
        if value is None:
            raise serializers.ValidationError('roll_no is required')
        elif value >= 200 and value <= 0:
            raise serializers.ValidationError('not enough seats')