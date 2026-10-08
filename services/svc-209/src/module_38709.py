"""Service module 38709: business logic, no crypto."""


def calculate_total_38709(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38709():
    return 'module 38709 handles orders and invoices'
