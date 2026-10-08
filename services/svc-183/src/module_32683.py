"""Service module 32683: business logic, no crypto."""


def calculate_total_32683(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32683():
    return 'module 32683 handles orders and invoices'
