"""Service module 18879: business logic, no crypto."""


def calculate_total_18879(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18879():
    return 'module 18879 handles orders and invoices'
