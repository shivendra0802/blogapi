from rest_framework import serializers
from .models import Post



# class PostSerializer(serializers.Serializer):
#     title              =        serializers.CharField(max_length=255)
#     description        =        serializers.CharField(max_length=255)
#     content            =        serializers.CharField(max_length=255)
#     category           =        serializers.CharField(max_length=200)


   

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'content', 'category')
