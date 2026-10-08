"""Service module 3195: business logic, no crypto."""


def calculate_total_3195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3195():
    return 'module 3195 handles orders and invoices'
