import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_KEY


def create_stripe_product(course):
    """func to create stripe product"""
    return stripe.Product.create(name=course.title)


def create_stripe_price(product, amount_pay):
    """func to create stripe price for product"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=int(amount_pay),
        product=product.get('id'),
    )


def create_stripe_session(price):
    return stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/lms/course/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
