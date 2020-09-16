from rest_framework import serializers
from api import models
#Helps to convert the python objects into a proper json object

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    roll_no = serializers.IntegerField()
    marks = serializers.IntegerField()


##Model serializer provide a class Meta which saves us from creating the
#fields of models again in serializers
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__' 