"""Service module 25749: business logic, no crypto."""


def calculate_total_25749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25749():
    return 'module 25749 handles orders and invoices'
