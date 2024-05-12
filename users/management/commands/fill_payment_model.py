from django.core.management import BaseCommand
from users.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment_list = [
            {"payment_date": "2020-10-10", "amount_pay": 1000, "type_payment": "CASH"},
            {"payment_date": "2020-05-05", "amount_pay": 2000, "type_payment": "CARD"}
        ]
        payments_for_create = []
        for p in payment_list:
            payments_for_create.append(
                Payment(**p)
            )
        Payment.objects.bulk_create(payments_for_create)
