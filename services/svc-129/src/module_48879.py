"""Service module 48879: business logic, no crypto."""


def calculate_total_48879(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48879():
    return 'module 48879 handles orders and invoices'
