"""Service module 28690: business logic, no crypto."""


def calculate_total_28690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28690():
    return 'module 28690 handles orders and invoices'
