"""Service module 1438: business logic, no crypto."""


def calculate_total_1438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1438():
    return 'module 1438 handles orders and invoices'
