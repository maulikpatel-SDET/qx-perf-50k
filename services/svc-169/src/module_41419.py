"""Service module 41419: business logic, no crypto."""


def calculate_total_41419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41419():
    return 'module 41419 handles orders and invoices'
