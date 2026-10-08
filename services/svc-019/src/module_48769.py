"""Service module 48769: business logic, no crypto."""


def calculate_total_48769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48769():
    return 'module 48769 handles orders and invoices'
