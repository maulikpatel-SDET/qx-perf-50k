"""Service module 45690: business logic, no crypto."""


def calculate_total_45690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45690():
    return 'module 45690 handles orders and invoices'
