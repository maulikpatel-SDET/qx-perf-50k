"""Service module 19321: business logic, no crypto."""


def calculate_total_19321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19321():
    return 'module 19321 handles orders and invoices'
