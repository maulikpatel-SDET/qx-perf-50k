"""Service module 3999: business logic, no crypto."""


def calculate_total_3999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3999():
    return 'module 3999 handles orders and invoices'
