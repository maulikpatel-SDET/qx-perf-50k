"""Service module 4970: business logic, no crypto."""


def calculate_total_4970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4970():
    return 'module 4970 handles orders and invoices'
