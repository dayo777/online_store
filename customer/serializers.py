from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Customer
        fields = ['name', 'customer_type', 'email', 'password', 'phone', 'address', 'created_at', 'updated_at']
    #
    # def create(self, validated_data):
    #     """
    #     Create and update a new 'Customer' instance, given the validated data
    #     """
    #     return Customer.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return and existing 'Customer' instance, given the validated data
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.customer_type = validated_data.get('customer_type', instance.customer_type)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.phone_number = validated_data.get('phone', instance.phone_number)
    #     instance.updated_at = validated_data.get('updated_at', instance.updated_at)
    #     instance.save()
    #     return instance

# class CustomerListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['name', 'customer_type', 'email', 'phone', 'address', 'created_at', 'updated_at']