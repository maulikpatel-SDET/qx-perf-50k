"""Service module 49962: business logic, no crypto."""


def calculate_total_49962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49962():
    return 'module 49962 handles orders and invoices'
