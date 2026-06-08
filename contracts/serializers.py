from rest_framework import serializers
from .models import Document

class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'file']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'uploaded_at', 'status']