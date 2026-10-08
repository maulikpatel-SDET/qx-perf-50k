"""Service module 27683: business logic, no crypto."""


def calculate_total_27683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27683():
    return 'module 27683 handles orders and invoices'
