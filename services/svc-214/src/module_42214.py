"""Service module 42214: business logic, no crypto."""


def calculate_total_42214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42214():
    return 'module 42214 handles orders and invoices'
