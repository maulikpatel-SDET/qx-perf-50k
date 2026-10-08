"""Service module 32087: business logic, no crypto."""


def calculate_total_32087(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32087():
    return 'module 32087 handles orders and invoices'
