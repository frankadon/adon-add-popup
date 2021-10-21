from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import CardDataSerialiser
from .models import CardData
from django.http import Http404
from django.shortcuts import render
# Create your views here.


class CardList(APIView):
    queryset = CardData.objects.all().order_by('-created')
    serializer_class = CardDataSerialiser
    # authentication_classes(TokenAuthentication)
    # permission_classes(permissions.IsAuthenticated)

    def get_queryset(self):
        return CardData.objects.filter(user=self.request.user)

    def get(self, request, format=None):
        cards = CardData.objects.all()
        serializer = CardDataSerialiser(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     serializer = CardDataSerialiser(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=self.request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardDetails(APIView):
    queryset = CardData.objects.all().order_by('-created')
    serializer_class = CardDataSerialiser
    # authentication_classes(TokenAuthentication)
    # permission_classes(permissions.IsAuthenticated)

    def get_object(self, ref_code):
        try:
            return CardData.objects.get(ref_code=ref_code)
        except CardData.DoesNotExist:
            raise Http404

    def get(self, request, ref_code, format=None):
        card = self.get_object(ref_code)
        serializer = CardDataSerialiser(card)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     card = self.get_object(pk)
    #     serializer = CardDataSerialiser(card, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     card = self.get_object(pk)
    #     card.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


def card_list(request):
    cards = CardData.objects.all().order_by('-created')
    context = {
        "title": "card list",
        "cards": cards,
    }
    return render(request, "card_list.html", context)
