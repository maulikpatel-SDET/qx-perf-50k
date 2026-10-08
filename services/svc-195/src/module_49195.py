"""Service module 49195: business logic, no crypto."""


def calculate_total_49195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49195():
    return 'module 49195 handles orders and invoices'
