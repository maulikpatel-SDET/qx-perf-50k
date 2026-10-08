"""Service module 1613: business logic, no crypto."""


def calculate_total_1613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1613():
    return 'module 1613 handles orders and invoices'
