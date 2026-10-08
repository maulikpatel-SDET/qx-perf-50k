"""Service module 17651: business logic, no crypto."""


def calculate_total_17651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17651():
    return 'module 17651 handles orders and invoices'
