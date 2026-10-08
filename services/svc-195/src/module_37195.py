"""Service module 37195: business logic, no crypto."""


def calculate_total_37195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37195():
    return 'module 37195 handles orders and invoices'
