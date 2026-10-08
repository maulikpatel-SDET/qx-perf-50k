"""Service module 13813: business logic, no crypto."""


def calculate_total_13813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13813():
    return 'module 13813 handles orders and invoices'
