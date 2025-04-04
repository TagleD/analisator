from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'name',
        'created_at',
    )
    list_display_links = (
        'id',
        'user',
        'name',
        'created_at',
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'report',
        'time',
        'amount',
        'is_fraud',
        'explanation',
        'transaction_varchar_id',
    )
    list_display_links = (
        'id',
        'report',
        'time',
        'amount',
        'is_fraud',
        'explanation',
        'transaction_varchar_id',
    )