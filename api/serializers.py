from rest_framework import serializers

#Helps to convert the python objects into a proper json object

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    roll_no = serializers.IntegerField()
    marks = serializers.IntegerField()