"""Service module 28977: business logic, no crypto."""


def calculate_total_28977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28977():
    return 'module 28977 handles orders and invoices'
