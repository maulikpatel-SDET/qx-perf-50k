"""Service module 22879: business logic, no crypto."""


def calculate_total_22879(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22879():
    return 'module 22879 handles orders and invoices'
