"""Service module 41415: business logic, no crypto."""


def calculate_total_41415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41415():
    return 'module 41415 handles orders and invoices'
