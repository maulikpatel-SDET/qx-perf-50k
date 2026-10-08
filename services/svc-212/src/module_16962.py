"""Service module 16962: business logic, no crypto."""


def calculate_total_16962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16962():
    return 'module 16962 handles orders and invoices'
