"""Service module 35999: business logic, no crypto."""


def calculate_total_35999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35999():
    return 'module 35999 handles orders and invoices'
