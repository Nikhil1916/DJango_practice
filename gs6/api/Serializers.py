from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
        
    def starts_with_r(value):
        if(value[0].lower()=='r'):
            raise serializers.ValidationError("Name should not start with r")
    
    # if u want a particular validation then you have to write separately
    
    # if one field is read only then
    
    name = serializers.CharField(default=None,validators=[starts_with_r])
    
    
    class Meta:
        model = Student
        fields = ['name', 'city','id','roll_no']
        # if multiple fields are read only
        # read_only_fields = ['name', 'city']
        
        # other way to add diff prope
        # extra_kwargs = {'name':{'read_only':True}}
        
    # validations 
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
            

        
    # no need to write create and update for model serializer
    