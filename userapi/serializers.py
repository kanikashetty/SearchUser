from .models import UserDetails
from django.utils.six import BytesIO
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField()
    #login = serializers.PrimaryKeyRelatedField(queryset=UserDetails.objects.all())
    class Meta:
        model = UserDetails
        #fields = ('login','id','repos_url','name','company','email','public_repos','created_at','updated_at')
        fields = '__all__'
        
    def create(self, validated_data):
        print "update"
        print validated_data
        result,created = UserDetails.objects.update_or_create(
            login = validated_data.get('login'),
            defaults = validated_data)
        return result
    
