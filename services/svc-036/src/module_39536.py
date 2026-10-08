"""Service module 39536: business logic, no crypto."""


def calculate_total_39536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39536():
    return 'module 39536 handles orders and invoices'
