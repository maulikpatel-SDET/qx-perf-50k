"""Service module 18214: business logic, no crypto."""


def calculate_total_18214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18214():
    return 'module 18214 handles orders and invoices'
