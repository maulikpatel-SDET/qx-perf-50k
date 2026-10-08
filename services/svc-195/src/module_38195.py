"""Service module 38195: business logic, no crypto."""


def calculate_total_38195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38195():
    return 'module 38195 handles orders and invoices'
