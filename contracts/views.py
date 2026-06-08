from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import DocumentUploadSerializer, DocumentSerializer

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
            return Response({
                'message': 'Upload successful!',
                'document_id': doc.id,
                'status': doc.status
            }, status=201)

        return Response(serializer.errors, status=400)

# Saare documents ki list
class DocumentListView(APIView):
    def get(self, request):
        docs = Document.objects.all().order_by('-uploaded_at')
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)