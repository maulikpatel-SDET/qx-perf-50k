"""Service module 38335: business logic, no crypto."""


def calculate_total_38335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38335():
    return 'module 38335 handles orders and invoices'
