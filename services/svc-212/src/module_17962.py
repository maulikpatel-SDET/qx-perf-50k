"""Service module 17962: business logic, no crypto."""


def calculate_total_17962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17962():
    return 'module 17962 handles orders and invoices'
