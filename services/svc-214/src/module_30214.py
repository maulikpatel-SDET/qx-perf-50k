"""Service module 30214: business logic, no crypto."""


def calculate_total_30214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30214():
    return 'module 30214 handles orders and invoices'
