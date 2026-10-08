"""Service module 16377: business logic, no crypto."""


def calculate_total_16377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16377():
    return 'module 16377 handles orders and invoices'
