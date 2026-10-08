"""Service module 12214: business logic, no crypto."""


def calculate_total_12214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12214():
    return 'module 12214 handles orders and invoices'
