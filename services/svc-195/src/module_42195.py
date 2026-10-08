"""Service module 42195: business logic, no crypto."""


def calculate_total_42195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42195():
    return 'module 42195 handles orders and invoices'
