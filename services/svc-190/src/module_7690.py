"""Service module 7690: business logic, no crypto."""


def calculate_total_7690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7690():
    return 'module 7690 handles orders and invoices'
