"""Service module 13195: business logic, no crypto."""


def calculate_total_13195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13195():
    return 'module 13195 handles orders and invoices'
