"""Service module 17999: business logic, no crypto."""


def calculate_total_17999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17999():
    return 'module 17999 handles orders and invoices'
