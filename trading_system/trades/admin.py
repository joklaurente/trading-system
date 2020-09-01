from django.contrib import admin
from trades.models import Trade, Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ('oid', 'name', 'price')


class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'stock', 'quantity')


admin.site.register(Stock, StockAdmin)
admin.site.register(Trade, TradeAdmin)
