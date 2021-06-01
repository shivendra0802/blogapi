from datetime import date
from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import serializers, status
from rest_framework.views import APIView
from .models import Post
from rest_framework.generics import GenericAPIView, ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin




class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# using genericapi view
# class PostGeneList(ListCreateAPIView, ListModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class PostGeneCreate(ListCreateAPIView, CreateModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class PostGeneRetrive(ListCreateAPIView, RetrieveModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class PostGeneUpdate(ListCreateAPIView, UpdateModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


# class PostGenDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# # using APIview  .
# class PostAPI(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             pst = Post.objects.get(id=id)
#             serializer = PostSerializer(pst)
#             return Response(serializer.data)

#         pst = Post.objects.all()
#         serializer = PostSerializer(pst, many=True)
#         return Response(serializer.data)


#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, pk, format=None):
#         id = pk
#         pst = Post.objects.get(pk=id)
#         serializer = PostSerializer(pst, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated'}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def patch(self, request, pk, format=None):
#         id = pk
#         pst = Post.objects.get(pk=id)
#         serializer = PostSerializer(pst, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     def delete(self, request, pk, format=None):
#         id = pk
#         pst = Post.objects.get(pk=id)
#         pst.delete()
#         return Response({'msg': 'Data Deleted'})





