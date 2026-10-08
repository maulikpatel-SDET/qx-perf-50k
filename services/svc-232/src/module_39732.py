"""Service module 39732: business logic, no crypto."""


def calculate_total_39732(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39732():
    return 'module 39732 handles orders and invoices'
