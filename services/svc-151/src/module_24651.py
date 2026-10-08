"""Service module 24651: business logic, no crypto."""


def calculate_total_24651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24651():
    return 'module 24651 handles orders and invoices'
