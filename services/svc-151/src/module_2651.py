"""Service module 2651: business logic, no crypto."""


def calculate_total_2651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2651():
    return 'module 2651 handles orders and invoices'
