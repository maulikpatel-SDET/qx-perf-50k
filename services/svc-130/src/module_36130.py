"""Service module 36130: business logic, no crypto."""


def calculate_total_36130(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36130():
    return 'module 36130 handles orders and invoices'
