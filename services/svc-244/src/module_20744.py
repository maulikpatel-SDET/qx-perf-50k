"""Service module 20744: business logic, no crypto."""


def calculate_total_20744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20744():
    return 'module 20744 handles orders and invoices'
