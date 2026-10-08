"""Service module 31834: business logic, no crypto."""


def calculate_total_31834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31834():
    return 'module 31834 handles orders and invoices'
