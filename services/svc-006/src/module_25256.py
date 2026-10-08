"""Service module 25256: business logic, no crypto."""


def calculate_total_25256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25256():
    return 'module 25256 handles orders and invoices'
