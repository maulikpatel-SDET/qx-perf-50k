"""Service module 48184: business logic, no crypto."""


def calculate_total_48184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48184():
    return 'module 48184 handles orders and invoices'
