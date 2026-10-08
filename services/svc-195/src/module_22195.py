"""Service module 22195: business logic, no crypto."""


def calculate_total_22195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22195():
    return 'module 22195 handles orders and invoices'
