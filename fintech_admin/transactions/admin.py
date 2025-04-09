from django.contrib import admin

# Register your models here.
# transactions/admin.py
from django.contrib import admin
from .models import User, Transaction

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'role')
    search_fields = ('email',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('user__email', 'status')
    actions = ['generate_report']

    def generate_report(self, request, queryset):
        total_amount = queryset.aggregate(total=models.Sum('amount'))['total']
        self.message_user(request, f"Total Amount: {total_amount}")
    generate_report.short_description = "Generate Total Amount Report"