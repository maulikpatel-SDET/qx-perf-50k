"""Service module 12999: business logic, no crypto."""


def calculate_total_12999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12999():
    return 'module 12999 handles orders and invoices'
