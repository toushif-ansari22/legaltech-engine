from rest_framework import serializers
from .models import Document, ExtractedClause, RiskFlag

class RiskFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFlag
        fields = ['id', 'keyword', 'risk_level', 'flagged_at']

class ExtractedClauseSerializer(serializers.ModelSerializer):
    flags = RiskFlagSerializer(many=True, read_only=True)

    class Meta:
        model = ExtractedClause
        fields = ['id', 'clause_type', 'content', 'page_number', 'flags']

class DocumentSerializer(serializers.ModelSerializer):
    clauses = ExtractedClauseSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'uploaded_at', 'status', 'clauses']

class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'file']