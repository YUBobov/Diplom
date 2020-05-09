from django.contrib import admin

from .forms import FTTxForm
from .models import FTTx

@admin.register(FTTx)
class FTTxAdmin(admin.ModelAdmin):
    list_display = ('name','volokno','kN','price','link')
    list_filter = ('volokno','price')
    form = FTTxForm