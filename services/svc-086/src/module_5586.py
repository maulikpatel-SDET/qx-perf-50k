"""Service module 5586: business logic, no crypto."""


def calculate_total_5586(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5586():
    return 'module 5586 handles orders and invoices'
