"""Service module 26543: business logic, no crypto."""


def calculate_total_26543(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26543():
    return 'module 26543 handles orders and invoices'
