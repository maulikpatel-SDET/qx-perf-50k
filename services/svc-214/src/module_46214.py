"""Service module 46214: business logic, no crypto."""


def calculate_total_46214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46214():
    return 'module 46214 handles orders and invoices'
