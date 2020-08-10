from django.shortcuts import render
from .models import *
from .serializer import *
from .permissions import *
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ObjectPermission]


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([ObjectPermission])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Object Level permission need to check by your self
    object_permission = ObjectPermission()
    
    if not object_permission.has_object_permission(request, post_detail, post):
        print('No Object Permission')
        raise PermissionDenied

    serializer = PostSerializer(post)
    return Response(serializer.data)