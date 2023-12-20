from rest_framework import serializers
from .models import Student


# priority -> VALIDATORS, FIELD LEVEL VALIDATION, OBJECT LEVEL VALIDATION 

# VALIDATORS
def starts_with_r(value):
    if(value[0].lower()=='r'):
        raise serializers.ValidationError("Name should not start with r")
            

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_r])
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    
    # VALIDATIONS
    
    
    # field level validation
    # for validating one field
    # get auto invoked when is_valid() is called
    def validate_roll_no(self, value):
        if value is not None:
            if value >= 200:
                raise serializers.ValidationError('not enough seats')
        return value
    
    
    # OBJECT LEVEL VALIDATION
    # here data is dictionary of field values
    def validate(self, data):
        name = data.get('name', None)
        city = data.get('city', None)
        roll_no = data.get('roll_no', None)
        if name is not None and city.lower() == 'ranchi':
            raise serializers.ValidationError("City Ranchi is not allowed")
        # elif roll_no is not None and roll_no < Student.objects.filter(roll_no=roll_no).count > 0:
        #     raise serializers.ValidationError("Roll No already registered")
        return data
    