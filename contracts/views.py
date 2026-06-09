from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document, ExtractedClause, RiskFlag
from .serializers import DocumentUploadSerializer, DocumentSerializer
from .utils import extract_text_from_pdf, split_into_paragraphs, extract_entities, flag_risky_clauses

class DocumentUploadView(APIView):
    def post(self, request):
        serializer = DocumentUploadSerializer(data=request.data)

        if serializer.is_valid():
            file = request.FILES.get('file')
            if not file.name.endswith('.pdf'):
                return Response({'error': 'Sirf PDF upload karo!'}, status=400)

            doc = serializer.save()

            # Step 1: Text extract karo
            pdf_path = doc.file.path
            extracted_text = extract_text_from_pdf(pdf_path)
            paragraphs = split_into_paragraphs(extracted_text)

            # Step 2: Entities nikalo (company names, dates)
            entities = extract_entities(extracted_text)

            # Step 3: Risky clauses flag karo
            risky_clauses = flag_risky_clauses(paragraphs)

            # Step 4: Database mein save karo
            for item in risky_clauses:
                clause = ExtractedClause.objects.create(
                    document=doc,
                    clause_type='risk',
                    content=item['text'],
                    page_number=1
                )
                RiskFlag.objects.create(
                    clause=clause,
                    risk_level=item['risk_level'],
                    keyword=item['keyword']
                )

            # Status update karo
            doc.status = 'processed'
            doc.save()

            return Response({
                'message': 'Upload aur NLP extraction successful!',
                'document_id': doc.id,
                'status': doc.status,
                'entities': entities,
                'total_risky_clauses': len(risky_clauses),
                'risky_clauses': risky_clauses
            }, status=201)

        return Response(serializer.errors, status=400)

class DocumentListView(APIView):
    def get(self, request):
        docs = Document.objects.all().order_by('-uploaded_at')
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)