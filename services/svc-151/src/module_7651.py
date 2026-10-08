"""Service module 7651: business logic, no crypto."""


def calculate_total_7651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7651():
    return 'module 7651 handles orders and invoices'
