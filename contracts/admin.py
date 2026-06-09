from django.contrib import admin
from .models import Document, ExtractedClause, RiskFlag

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'uploaded_at']
    list_filter = ['status']
    search_fields = ['title']

@admin.register(ExtractedClause)
class ExtractedClauseAdmin(admin.ModelAdmin):
    list_display = ['clause_type', 'document', 'page_number']
    list_filter = ['clause_type']
    search_fields = ['content']

@admin.register(RiskFlag)
class RiskFlagAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'risk_level', 'clause', 'flagged_at']
    list_filter = ['risk_level']
    search_fields = ['keyword']