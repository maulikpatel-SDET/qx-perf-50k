"""Service module 14214: business logic, no crypto."""


def calculate_total_14214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14214():
    return 'module 14214 handles orders and invoices'
