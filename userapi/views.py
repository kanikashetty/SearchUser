 
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,MultiPartParser  
from rest_framework import viewsets,status
from  .models import UserDetails
from .serializers import UserSerializer
import requests
import json
import logging

logger = logging.getLogger(__name__)

@api_view(['GET','POST'])
@parser_classes((JSONParser,MultiPartParser))

def searchUser(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            created = request.data.get('created')
            print name,created
            if name:
                req = requests.get('https://api.github.com/users/'+name)
                data = json.loads(req.content)
                serializer = UserSerializer(data=data)
            elif created:
                req = requests.get('https://api.github.com/search/users?q=created:'+created)
                jsonData = json.loads(req.content)
                data = jsonData['items']
                serializer = UserSerializer(data=data,many=True)
            if serializer.is_valid():
                print 'user update'
                serializer.save()
                logger.info('Posted the user data')
                return Response({'serializer':serializer.data})
            logger.error('error occured while validating data')
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'GET':
                user = UserDetails.objects.all()
                serializer = UserSerializer(user,many=True)  
                logger.info('GET request to list the stored users')
                return Response({'serializer':serializer.data})
    except Exception as e:
        logger.exception(e)
        return Response(e,status=status.HTTP_400_BAD_REQUEST)

