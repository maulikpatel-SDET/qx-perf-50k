"""Service module 49214: business logic, no crypto."""


def calculate_total_49214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49214():
    return 'module 49214 handles orders and invoices'
