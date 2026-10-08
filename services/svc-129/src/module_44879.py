"""Service module 44879: business logic, no crypto."""


def calculate_total_44879(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44879():
    return 'module 44879 handles orders and invoices'
