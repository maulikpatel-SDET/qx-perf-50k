"""Service module 14888: business logic, no crypto."""


def calculate_total_14888(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14888():
    return 'module 14888 handles orders and invoices'
