from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.base import ContentFile
from .models import Media


@api_view(['POST'])
def upload_file(request):
    print("File Uploaded from flutter!")

    print(request.FILES)
    print("\n")
    print(request.FILES['file'])


    toUpload = Media(media=request.FILES['file'])  
    toUpload.save()

    #return Response(status=status.HTTP_200_OK)
    return JsonResponse({'media_url':toUpload.media.name})


class UserViewSet(viewsets.ModelViewSet):
    pass