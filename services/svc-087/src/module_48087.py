"""Service module 48087: business logic, no crypto."""


def calculate_total_48087(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48087():
    return 'module 48087 handles orders and invoices'
