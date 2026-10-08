"""Service module 35438: business logic, no crypto."""


def calculate_total_35438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35438():
    return 'module 35438 handles orders and invoices'
