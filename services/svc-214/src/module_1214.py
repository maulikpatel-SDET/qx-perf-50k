"""Service module 1214: business logic, no crypto."""


def calculate_total_1214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1214():
    return 'module 1214 handles orders and invoices'
