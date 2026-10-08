"""Service module 21910: business logic, no crypto."""


def calculate_total_21910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21910():
    return 'module 21910 handles orders and invoices'
