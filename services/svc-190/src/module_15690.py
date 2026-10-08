"""Service module 15690: business logic, no crypto."""


def calculate_total_15690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15690():
    return 'module 15690 handles orders and invoices'
