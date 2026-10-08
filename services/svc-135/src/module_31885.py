"""Service module 31885: business logic, no crypto."""


def calculate_total_31885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31885():
    return 'module 31885 handles orders and invoices'
