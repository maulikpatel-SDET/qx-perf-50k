"""Service module 12621: business logic, no crypto."""


def calculate_total_12621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12621():
    return 'module 12621 handles orders and invoices'
