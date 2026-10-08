"""Service module 37690: business logic, no crypto."""


def calculate_total_37690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37690():
    return 'module 37690 handles orders and invoices'
