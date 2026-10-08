"""Service module 3101: business logic, no crypto."""


def calculate_total_3101(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3101():
    return 'module 3101 handles orders and invoices'
