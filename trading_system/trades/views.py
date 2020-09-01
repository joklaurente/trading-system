from trades.models import Trade, Stock
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from trades.serializers import TradeBuySerializer, TradeSellSerializer


class TradeListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        stocks = Trade.objects.filter(
            user=request.user).values("stock__name", "quantity")
        print(stocks)
        return Response(
            stocks,
            status=status.HTTP_200_OK,
        )


class TradeTotalView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        stock_id = self.request.GET.get('stock_id')

        if not stock_id:
            return Response(
                "Stock ID is required",
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Stock.objects.filter(oid=stock_id):
            return Response(
                "Invalid stock ID",
                status=status.HTTP_400_BAD_REQUEST
            )

        trade = Trade.objects.filter(
            user=request.user, stock__oid=stock_id).first()

        if not trade:
            return Response(
                "Stock not available for the user",
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                'stock': trade.stock.name,
                'total': trade.get_total(),
            },
            status=status.HTTP_200_OK,
        )


class TradeBuyView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # serializer = TradeBuySerializer(data=request.data)
        serializer = TradeBuySerializer(
            data=request.data,
            context={
                'request': request
            },
        )
        if serializer.is_valid():
            serializer.save()
            message = 'Stock has been bought'
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TradeSellView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = TradeSellSerializer(
            data=request.data,
            context={
                'request': request
            },
        )
        if serializer.is_valid():
            serializer.save()
            message = 'Stock has been sold'
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
