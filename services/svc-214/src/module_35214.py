"""Service module 35214: business logic, no crypto."""


def calculate_total_35214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35214():
    return 'module 35214 handles orders and invoices'
