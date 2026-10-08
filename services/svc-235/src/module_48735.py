"""Service module 48735: business logic, no crypto."""


def calculate_total_48735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48735():
    return 'module 48735 handles orders and invoices'
