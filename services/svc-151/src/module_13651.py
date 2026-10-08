"""Service module 13651: business logic, no crypto."""


def calculate_total_13651(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13651():
    return 'module 13651 handles orders and invoices'
