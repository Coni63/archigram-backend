from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import POCSerializer
from .models import POCModel
from rest_framework.decorators import action


class POCViewSet(viewsets.ModelViewSet):
    serializer_class = POCSerializer

    def get_queryset(self):
        """Required for permission classes."""
        return POCModel.objects.all()

    @action(detail=False, methods=['get', 'post'], url_path='project/(?P<project_id>[^/.]+)')
    def project(self, request, project_id=None):
        """Handle both GET and POST for a project's POC."""
        if request.method == 'GET':
            return self._get_by_project(request, project_id)
        elif request.method == 'POST':
            return self._create_version(request, project_id)
    
    def _get_by_project(self, request, project_id):
        """Get POC for a project. Returns latest version by default."""
        version = request.query_params.get('version')
        
        if version:
            # Get specific version
            poc = get_object_or_404(
                POCModel,
                project_id=project_id,
                version=version
            )
        else:
            # Get latest version
            poc = POCModel.objects.filter(
                project_id=project_id
            ).order_by('-version').first()
            
            if not poc:
                return Response(
                    {'detail': 'No POC found for this project.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        
        serializer = self.serializer_class(poc)
        return Response(serializer.data)

    def _create_version(self, request, project_id):
        """Create a new version for a project."""
        # Add project_id to the data
        data = request.data.copy()
        data['project'] = project_id
        
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
