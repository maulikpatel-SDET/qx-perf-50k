"""Service module 41863: business logic, no crypto."""


def calculate_total_41863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41863():
    return 'module 41863 handles orders and invoices'
