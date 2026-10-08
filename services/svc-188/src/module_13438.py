"""Service module 13438: business logic, no crypto."""


def calculate_total_13438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13438():
    return 'module 13438 handles orders and invoices'
