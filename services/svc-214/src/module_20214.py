"""Service module 20214: business logic, no crypto."""


def calculate_total_20214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20214():
    return 'module 20214 handles orders and invoices'
