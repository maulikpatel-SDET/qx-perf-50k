"""Service module 15962: business logic, no crypto."""


def calculate_total_15962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15962():
    return 'module 15962 handles orders and invoices'
