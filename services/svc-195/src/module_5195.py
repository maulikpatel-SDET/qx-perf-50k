"""Service module 5195: business logic, no crypto."""


def calculate_total_5195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5195():
    return 'module 5195 handles orders and invoices'
