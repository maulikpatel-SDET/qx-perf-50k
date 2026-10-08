"""Service module 49087: business logic, no crypto."""


def calculate_total_49087(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49087():
    return 'module 49087 handles orders and invoices'
