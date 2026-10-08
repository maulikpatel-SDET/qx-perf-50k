"""Service module 11214: business logic, no crypto."""


def calculate_total_11214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11214():
    return 'module 11214 handles orders and invoices'
