"""Service module 20999: business logic, no crypto."""


def calculate_total_20999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20999():
    return 'module 20999 handles orders and invoices'
