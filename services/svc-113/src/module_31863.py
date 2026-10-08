"""Service module 31863: business logic, no crypto."""


def calculate_total_31863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31863():
    return 'module 31863 handles orders and invoices'
