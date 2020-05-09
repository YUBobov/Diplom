from django.contrib import admin

from .forms import FTTxForm
from .models import FTTx
from .forms import ADSSForm
from .models import ADSS

@admin.register(FTTx)
class FTTxAdmin(admin.ModelAdmin):
    list_display = ('name','volokno','kN','price','link')
    list_filter = ('volokno','price')
    form = FTTxForm

@admin.register(ADSS)
class ADSSAdmin(admin.ModelAdmin):
    list_display = ('name','volokno','kN','price','link')
    list_filter = ('volokno','price')
    form = ADSSForm