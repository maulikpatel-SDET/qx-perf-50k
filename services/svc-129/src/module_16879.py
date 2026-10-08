"""Service module 16879: business logic, no crypto."""


def calculate_total_16879(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16879():
    return 'module 16879 handles orders and invoices'
