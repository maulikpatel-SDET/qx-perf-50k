"""Service module 4999: business logic, no crypto."""


def calculate_total_4999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4999():
    return 'module 4999 handles orders and invoices'
