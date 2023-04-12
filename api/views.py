from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Parceiro
from api.repository import ParceiroRepository
from api.serializers import ParceiroSerializer
from api.utils import process_and_save_csv_values, validate_fields_partner


class ParceiroViewSet(viewsets.ModelViewSet):
    queryset = Parceiro.objects.all().order_by('nome_fantasia')
    serializer_class = ParceiroSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request,args,kwargs)

    def create(self, request,*args, **kwargs):
        try:
            validate_error = validate_fields_partner(request.data)
            if validate_error:
                return Response({'errors': validate_error}, status=status.HTTP_400_BAD_REQUEST)
            
            ParceiroRepository.save_partner(request.data)

            return Response(
                'Parceiro salvo/atualizado com sucesso!',
                status=status.HTTP_201_CREATED
                )

        except Exception as e:
            return Response(
                f'Houve um problema ao salvar o parceiro por {e}',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['post'], url_path='csv-upload')
    def csv_upload(self, request):
        csv_file = request.FILES.get('csv_file')
        if csv_file:
            errors =  process_and_save_csv_values(csv_file)
            if errors:
                return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'success': 'Parceiros cadastrados com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong file type'}, status=status.HTTP_400_BAD_REQUEST)

    