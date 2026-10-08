"""Service module 12453: business logic, no crypto."""


def calculate_total_12453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12453():
    return 'module 12453 handles orders and invoices'
