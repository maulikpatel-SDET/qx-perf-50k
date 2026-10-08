"""Service module 18789: business logic, no crypto."""


def calculate_total_18789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18789():
    return 'module 18789 handles orders and invoices'
