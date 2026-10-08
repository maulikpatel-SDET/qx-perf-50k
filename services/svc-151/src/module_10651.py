"""Service module 10651: business logic, no crypto."""


def calculate_total_10651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10651():
    return 'module 10651 handles orders and invoices'
