"""Service module 25101: business logic, no crypto."""


def calculate_total_25101(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25101():
    return 'module 25101 handles orders and invoices'
