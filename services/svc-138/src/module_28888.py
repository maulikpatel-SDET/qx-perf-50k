"""Service module 28888: business logic, no crypto."""


def calculate_total_28888(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28888():
    return 'module 28888 handles orders and invoices'
