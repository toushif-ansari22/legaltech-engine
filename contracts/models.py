from django.db import models

# Table 1: PDF document ki info store hogi
class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='contracts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.title

# Table 2: PDF se nikale gaye clauses
class ExtractedClause(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    clause_type = models.CharField(max_length=50)
    content = models.TextField()
    page_number = models.IntegerField(default=1)

    def __str__(self):
        return self.clause_type

# Table 3: Risky clauses flag honge yahan
class RiskFlag(models.Model):
    clause = models.ForeignKey(ExtractedClause, on_delete=models.CASCADE)
    risk_level = models.CharField(max_length=10)
    keyword = models.CharField(max_length=100)
    flagged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword
