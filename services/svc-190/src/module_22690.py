"""Service module 22690: business logic, no crypto."""


def calculate_total_22690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22690():
    return 'module 22690 handles orders and invoices'
