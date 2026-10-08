"""Service module 7813: business logic, no crypto."""


def calculate_total_7813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7813():
    return 'module 7813 handles orders and invoices'
