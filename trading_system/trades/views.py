from trades.models import Trade, Stock
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from trades.serializers import TradeBuySerializer, TradeSellSerializer, UserSerializer, StockSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TradeListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        stocks = Trade.objects.filter(
            user=request.user).values("stock__name", "quantity")
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
        serializer = TradeBuySerializer(
            data=request.data,
            context={
                'request': request
            },
        )
        data = {}
        if serializer.is_valid():
            trade = serializer.save()
            stock = Stock.objects.get(name=trade.stock)
            data['transaction'] = 'Buy'
            data['stock_name'] = stock.name
            data['quantity'] = request.data['quantity']
            return Response(data, status=status.HTTP_201_CREATED)
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
        data = {}
        if serializer.is_valid():
            trade = serializer.save()
            stock = Stock.objects.get(name=trade.stock)
            data['transaction'] = 'Sell'
            data['stock_name'] = stock.name
            data['quantity'] = request.data['quantity']
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(
            data=request.data,
            context={
                'request': request
            },
        )

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        stocks = Stock.objects.all().values("oid", "name", "price")
        return Response(
            stocks,
            status=status.HTTP_200_OK,
        )


class StockCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
