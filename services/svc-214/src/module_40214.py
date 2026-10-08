"""Service module 40214: business logic, no crypto."""


def calculate_total_40214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40214():
    return 'module 40214 handles orders and invoices'
