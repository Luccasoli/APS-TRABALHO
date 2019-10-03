from ..Events.models import Events, ConcentrationArea, Keyword
from .serializers import ConcentrationAreaSerializer, KeywordSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(['POST'])
@permission_classes([AllowAny])
def new_concentration_area(request):
    """"""
    serializer = ConcentrationAreaSerializer(data=request.data)
    if serializer.is_valid():
        if ConcentrationArea.objects.filter(area=serializer.data['area']):
            js = {"Valid": False,
                    "reason": "Já existe essa area de concentração"}
            return Response(js)
        concentration_area = ConcentrationArea(**serializer.data)
        concentration_area.save()
        return Response({"Valid": True,
                         "Text": "Área de concentração criada com sucesso"})
    return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def new_keyword(request):
    """"""
    serializer = KeywordSerializer(data=request.data)
    if serializer.is_valid():
        if Keyword.objects.filter(keyword=serializer.data['keyword']):
            js = {"Valid": False,
                    "reason": "Já existe essa keyword"}
            return Response(js)
        keyword_ = Keyword(**serializer.data)
        keyword_.save()
        return Response({"Valid": True,
                         "Text": "Keyword criada com sucesso"})
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def keyword_list(request):
    """"""
    keywords = Keyword.objects.all()
    serializer = KeywordSerializer(keywords, many=True)
    print(serializer)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([AllowAny])
def concentration_area_list(request):
    """"""
    keywords = ConcentrationArea.objects.all()
    serializer = ConcentrationAreaSerializer(keywords, many=True)
    print(serializer)
    return JsonResponse(serializer.data, safe=False)