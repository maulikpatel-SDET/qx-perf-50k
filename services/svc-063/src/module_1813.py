"""Service module 1813: business logic, no crypto."""


def calculate_total_1813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1813():
    return 'module 1813 handles orders and invoices'
