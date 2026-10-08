"""Service module 4087: business logic, no crypto."""


def calculate_total_4087(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4087():
    return 'module 4087 handles orders and invoices'
