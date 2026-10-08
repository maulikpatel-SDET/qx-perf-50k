"""Service module 40438: business logic, no crypto."""


def calculate_total_40438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40438():
    return 'module 40438 handles orders and invoices'
