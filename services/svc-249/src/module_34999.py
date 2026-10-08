"""Service module 34999: business logic, no crypto."""


def calculate_total_34999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34999():
    return 'module 34999 handles orders and invoices'
