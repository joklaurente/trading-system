from rest_framework import serializers
from trades.models import Trade, Stock
from django.contrib.auth.models import User


class TradeBuySerializer(serializers.ModelSerializer):
    stock_id = serializers.CharField(max_length=200)
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = Trade
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        stock = Stock.objects.filter(oid=data['stock_id']).first()
        quantity = data['quantity']
        if not stock:
            raise serializers.ValidationError(
                {'stock': 'Invalid stock ID: %s' % (data['stock_id'])})
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        stock = Stock.objects.get(oid=self.validated_data.get('stock_id'))
        quantity = self.validated_data.get('quantity')
        trade = Trade.objects.filter(user=user, stock=stock).first()
        if trade:
            trade.quantity += quantity
            trade.save()
        else:
            trade = Trade.objects.create(
                user=user, stock=stock, quantity=quantity)
        return trade


class TradeSellSerializer(serializers.ModelSerializer):
    stock_id = serializers.CharField(max_length=200)
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = Trade
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        stock = Stock.objects.filter(oid=data['stock_id']).first()
        quantity = data['quantity']
        if not stock:
            raise serializers.ValidationError(
                {'stock': 'Invalid stock ID: %s' % (data['stock_id'])})

        trade = Trade.objects.filter(user=user, stock=stock).first()
        if not trade:
            raise serializers.ValidationError(
                {'stock': 'No available stock to sell'})

        if trade.quantity < quantity:
            raise serializers.ValidationError(
                {'stock': 'Insufficient stocks'})
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        stock = Stock.objects.get(oid=self.validated_data.get('stock_id'))
        quantity = self.validated_data.get('quantity')
        trade = Trade.objects.get(user=user, stock=stock)
        trade.quantity -= quantity
        trade.save()
        return trade


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('oid', 'name', 'price')
