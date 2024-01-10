from django import template

register = template.Library()

@register.filter
def convert_to_inr(price):
    # Replace this with your currency conversion logic
    exchange_rate = 75.0  # Replace with your desired exchange rate
    price_in_inr = price * exchange_rate
    return f"₹{price_in_inr:.2f}"
