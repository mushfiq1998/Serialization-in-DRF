from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=100)
	roll_number = serializers.IntegerField()
	institute = serializers.CharField(max_length=100)
	department= serializers.CharField(max_length=100)
	address = serializers.CharField(max_length=100)
