from django.contrib.auth.models import User, Group
from .models import Menu, MenuItem
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # override create to set a default password

        if 'is_staff' not in validated_data:  # is_staff == admin!
            validated_data['is_staff'] = False

        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            is_staff=validated_data['is_staff'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        # Set password same as the username
        user.set_password(validated_data['username'])
        user.save()

        # Note
        # Note that add(), create(), remove(), and clear() all apply database
        # changes immediately for all types of related fields. In other words,
        # there is no need to call save() on either end of the relationship.
        for group in validated_data['groups']:
            user.groups.add(group)

        return user

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name',
                  'email', 'is_staff', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('url', 'name', 'description', 'chef', 'available')


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('url', 'name', 'description', 'cost_to_make',
                  'sale_price', 'available', 'menu')
