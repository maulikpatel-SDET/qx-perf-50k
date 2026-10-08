"""Service module 44214: business logic, no crypto."""


def calculate_total_44214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44214():
    return 'module 44214 handles orders and invoices'
