"""Service module 15184: business logic, no crypto."""


def calculate_total_15184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15184():
    return 'module 15184 handles orders and invoices'
