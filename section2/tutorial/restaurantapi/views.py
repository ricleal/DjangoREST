from django.contrib.auth.models import User, Group
from django.shortcuts import render
from models import Menu, MenuItem
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from serializers import UserSerializer, GroupSerializer
from serializers import MenuSerializer, MenuItemSerializer

# for custom GET of available menu list
from rest_framework import mixins
from rest_framework import generics

# for custom GET of available menu details
from django.http import Http404
from rest_framework.exceptions import APIException
from rest_framework.response import Response 
from rest_framework.views import APIView 

# Create your views here.

class ForbiddenAccess(APIException):
	status_code = 403
	default_detail = 'Action Forbidden'  

class AvailableMenuDetail(APIView):

	permission_classes = ()

	def get_object(self, pk):
		try:
			return Menu.objects.get(pk=pk, available=True)

		except Menu.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		menu = self.get_object(pk)

		serializer = MenuSerializer(menu, context={'request':request})

		return Response(serializer.data)

	def put(self, request, pk, format=None):

		raise ForbiddenAccess 

	def delete(self, request, pk, format=None):

		raise ForbiddenAccess  

class AvailableMenuList(mixins.ListModelMixin, generics.GenericAPIView):

	permission_classes = ()
	queryset = Menu.objects.filter(available=True)
	serializer_class = MenuSerializer

	def get(self, request, *args, **kwargs):

		return self.list(request, *args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):

	permission_classes = (IsAdminUser,)

	queryset = User.objects.all()
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

	permission_classes = (IsAdminUser,)

	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class MenuViewSet(viewsets.ModelViewSet):

	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

class MenuItemViewSet(viewsets.ModelViewSet):

	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer