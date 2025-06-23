payments.py

import stripe

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

PRICE_MAPPING = { "basic": 59, "standard": 90, "premium": 120 }

def handle_payment(user_id: str, plan: str): amount = PRICE_MAPPING.get(plan.lower()) if not amount: raise Exception("Invalid plan selected") # Example using Stripe payment_intent = stripe.PaymentIntent.create( amount=amount * 100,  # Stripe uses cents currency="usd", metadata={"user_id": user_id, "plan": plan} ) return payment_intent.client_secret
