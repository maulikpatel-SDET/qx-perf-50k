"""Service module 29750: business logic, no crypto."""


def calculate_total_29750(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29750():
    return 'module 29750 handles orders and invoices'
