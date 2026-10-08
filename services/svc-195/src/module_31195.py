"""Service module 31195: business logic, no crypto."""


def calculate_total_31195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31195():
    return 'module 31195 handles orders and invoices'
