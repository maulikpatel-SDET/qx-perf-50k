"""Service module 38498: business logic, no crypto."""


def calculate_total_38498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38498():
    return 'module 38498 handles orders and invoices'
