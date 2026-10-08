"""Service module 37638: business logic, no crypto."""


def calculate_total_37638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37638():
    return 'module 37638 handles orders and invoices'
