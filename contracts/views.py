from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import DocumentUploadSerializer, DocumentSerializer
from .utils import extract_text_from_pdf, split_into_paragraphs
import os

# PDF upload karne ka API
class DocumentUploadView(APIView):
    def post(self, request):
        serializer = DocumentUploadSerializer(data=request.data)

        if serializer.is_valid():
            # Sirf PDF allow hai
            file = request.FILES.get('file')
            if not file.name.endswith('.pdf'):
                return Response({'error': 'Sirf PDF upload karo!'}, status=400)

            doc = serializer.save()

            # PDF se text extract karo
            pdf_path = doc.file.path
            extracted_text = extract_text_from_pdf(pdf_path)
            paragraphs = split_into_paragraphs(extracted_text)

            # Status update karo
            doc.status = 'processed'
            doc.save()

            return Response({
                'message': 'Upload aur extraction successful!',
                'document_id': doc.id,
                'status': doc.status,
                'total_paragraphs': len(paragraphs),
                'preview': paragraphs[:3]  # pehle 3 paragraphs dikhao
            }, status=201)

        return Response(serializer.errors, status=400)

# Saare documents ki list
class DocumentListView(APIView):
    def get(self, request):
        docs = Document.objects.all().order_by('-uploaded_at')
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)