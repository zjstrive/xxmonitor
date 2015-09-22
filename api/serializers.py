'''
Created on Sep 11, 2015

@author: jie
'''

from rest_framework import serializers
from api.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('unique_name', 'display_name')
