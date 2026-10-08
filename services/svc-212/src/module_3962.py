"""Service module 3962: business logic, no crypto."""


def calculate_total_3962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3962():
    return 'module 3962 handles orders and invoices'
