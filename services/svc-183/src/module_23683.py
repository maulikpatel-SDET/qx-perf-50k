"""Service module 23683: business logic, no crypto."""


def calculate_total_23683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23683():
    return 'module 23683 handles orders and invoices'
