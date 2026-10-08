"""Service module 32690: business logic, no crypto."""


def calculate_total_32690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32690():
    return 'module 32690 handles orders and invoices'
