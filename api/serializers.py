from rest_framework import serializers
from api import models
#Helps to convert the python objects into a proper json object

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    roll_no = serializers.IntegerField()
    marks = serializers.IntegerField()

#For tags we use another serializers
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


#Model serializer provide a class Meta which saves us from creating the
#fields of models again in serializers
class ArticleSerializer(serializers.ModelSerializer):
    #here read only is added because while deserializing the object to json we want to
    #keep our tag separate from the Article
    tags = TagSerializer(many =True,read_only = True)
    class Meta:
        model = models.Article
        fields = '__all__' 