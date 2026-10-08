"""Service module 46879: business logic, no crypto."""


def calculate_total_46879(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46879():
    return 'module 46879 handles orders and invoices'
