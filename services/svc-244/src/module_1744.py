"""Service module 1744: business logic, no crypto."""


def calculate_total_1744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1744():
    return 'module 1744 handles orders and invoices'
