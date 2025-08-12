# core/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Member, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        
        member = Member.objects.create(user=user)
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class TransactionDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    member = serializers.StringRelatedField()  # or MemberSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'
