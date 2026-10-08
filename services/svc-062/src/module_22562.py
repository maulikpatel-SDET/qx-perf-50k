"""Service module 22562: business logic, no crypto."""


def calculate_total_22562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22562():
    return 'module 22562 handles orders and invoices'
