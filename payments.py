import stripe

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"  # Replace with your real Stripe secret key

PRICE_MAPPING = {
    "basic": 5900,      # $59.00 (Stripe uses cents)
    "pro": 9000,        # $90.00
    "premium": 12000    # $120.00
}

def create_payment(user_id: str, plan: str):
    amount = PRICE_MAPPING.get(plan.lower())
    
    if not amount:
        raise Exception("Invalid plan selected")
    
    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        metadata={
            "user_id": user_id,
            "plan": plan
        }
    )

    return payment_intent.client_secret
