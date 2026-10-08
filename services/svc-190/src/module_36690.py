"""Service module 36690: business logic, no crypto."""


def calculate_total_36690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36690():
    return 'module 36690 handles orders and invoices'
