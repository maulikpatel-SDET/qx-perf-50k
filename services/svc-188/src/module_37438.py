"""Service module 37438: business logic, no crypto."""


def calculate_total_37438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37438():
    return 'module 37438 handles orders and invoices'
